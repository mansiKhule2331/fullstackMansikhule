"""
Seed script — run once to populate the database with sample data.
Usage:  python seed.py
"""
from pymongo import MongoClient
from bson import ObjectId
import bcrypt
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB  = os.getenv("MONGO_DB", "learnquiz")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

# ── Clear collections ─────────────────────────────────────────────
for col in ("users", "languages", "topics", "questions", "progress"):
    db[col].drop()
print("✓ Cleared old data")

# ── Users ─────────────────────────────────────────────────────────
def hash_pw(pw):
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

admin_id = ObjectId()
user1_id = ObjectId()
user2_id = ObjectId()

db.users.insert_many([
    {
        "_id": admin_id,
        "name": "Admin User",
        "email": "admin@learnquiz.com",
        "password": hash_pw("admin123"),
        "role": "admin",
        "last_login": datetime.utcnow(),
        "login_count": 5,
        "created_at": datetime.utcnow(),
    },
    {
        
    },
    {
       
    },
])
print("✓ Users seeded")

# ── Languages ─────────────────────────────────────────────────────
py_id  = ObjectId()
js_id  = ObjectId()
sql_id = ObjectId()

db.languages.insert_many([
    {"_id": py_id,  "language_name": "Python",     "description": "A versatile, beginner-friendly programming language used in web dev, data science, AI and more."},
    {"_id": js_id,  "language_name": "JavaScript", "description": "The language of the web. Powers interactive UIs, servers (Node.js), and mobile apps."},
    {"_id": sql_id, "language_name": "SQL",        "description": "Structured Query Language for managing and querying relational databases."},
])
print("✓ Languages seeded")

# ── Topics ────────────────────────────────────────────────────────
py_basics_id   = ObjectId()
py_oop_id      = ObjectId()
js_basics_id   = ObjectId()
js_async_id    = ObjectId()
sql_basics_id  = ObjectId()
sql_joins_id   = ObjectId()

db.topics.insert_many([
    {
        "_id": py_basics_id,
        "language_id": py_id,
        "topic_name": "Python Basics",
        "content": """## Python Basics

Python is a high-level, interpreted programming language known for its clean syntax and readability.

### Variables & Data Types
Python supports several built-in data types:
- **int**: Whole numbers → `x = 10`
- **float**: Decimal numbers → `y = 3.14`
- **str**: Text → `name = "Alice"`
- **bool**: True/False → `flag = True`
- **list**: Ordered collection → `nums = [1, 2, 3]`
- **dict**: Key-value pairs → `person = {"name": "Bob", "age": 25}`

### Control Flow
```python
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Less")
```

### Loops
```python
for i in range(5):
    print(i)

while x > 0:
    x -= 1
```

### Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```
""",
    },
    {
        "_id": py_oop_id,
        "language_id": py_id,
        "topic_name": "Object-Oriented Python",
        "content": """## Object-Oriented Python

OOP organises code into **classes** and **objects**.

### Classes & Objects
```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

dog = Animal("Dog", "Woof")
print(dog.speak())  # Dog says Woof
```

### Inheritance
```python
class Dog(Animal):
    def fetch(self):
        return f"{self.name} fetches the ball!"
```

### Encapsulation & Properties
```python
class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
```
""",
    },
    {
        "_id": js_basics_id,
        "language_id": js_id,
        "topic_name": "JavaScript Basics",
        "content": """## JavaScript Basics

JavaScript (JS) is the primary language for web interactivity.

### Variables
```js
let name = "Alice";     // block-scoped, re-assignable
const PI = 3.14;        // block-scoped, constant
var legacy = "old way"; // function-scoped (avoid in modern JS)
```

### Functions
```js
// Regular function
function add(a, b) { return a + b; }

// Arrow function
const multiply = (a, b) => a * b;
```

### Arrays & Objects
```js
const fruits = ["apple", "banana", "cherry"];
fruits.forEach(f => console.log(f));

const user = { name: "Bob", age: 30 };
console.log(user.name); // Bob
```

### DOM Manipulation
```js
document.getElementById("btn").addEventListener("click", () => {
    alert("Clicked!");
});
```
""",
    },
    {
        "_id": js_async_id,
        "language_id": js_id,
        "topic_name": "Async JavaScript",
        "content": """## Async JavaScript

JavaScript is single-threaded but handles async work via callbacks, Promises and async/await.

### Promises
```js
fetch("https://api.example.com/data")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
```

### Async / Await
```js
async function loadUser(id) {
    try {
        const res = await fetch(`/api/users/${id}`);
        const user = await res.json();
        return user;
    } catch (error) {
        console.error("Failed:", error);
    }
}
```

### Event Loop
JavaScript uses an **event loop** to handle non-blocking I/O. Microtasks (Promises) are processed before the next task in the queue.
""",
    },
    {
        "_id": sql_basics_id,
        "language_id": sql_id,
        "topic_name": "SQL Basics",
        "content": """## SQL Basics

SQL is used to create, read, update and delete data in relational databases.

### SELECT
```sql
SELECT name, email FROM users WHERE age > 18;
SELECT * FROM products ORDER BY price DESC LIMIT 10;
```

### INSERT
```sql
INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 25);
```

### UPDATE
```sql
UPDATE users SET age = 26 WHERE email = 'alice@example.com';
```

### DELETE
```sql
DELETE FROM users WHERE id = 5;
```

### Aggregate Functions
```sql
SELECT COUNT(*) FROM orders;
SELECT AVG(price), MAX(price), MIN(price) FROM products;
SELECT category, SUM(sales) FROM products GROUP BY category;
```
""",
    },
    {
        "_id": sql_joins_id,
        "language_id": sql_id,
        "topic_name": "SQL Joins",
        "content": """## SQL Joins

Joins combine rows from two or more tables based on a related column.

### INNER JOIN — only matching rows
```sql
SELECT orders.id, users.name
FROM orders
INNER JOIN users ON orders.user_id = users.id;
```

### LEFT JOIN — all left rows + matching right rows
```sql
SELECT users.name, orders.total
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

### RIGHT JOIN & FULL OUTER JOIN
Similar to LEFT JOIN but from the right / both sides.

### Self Join
```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```
""",
    },
])
print("✓ Topics seeded")

# ── Questions ─────────────────────────────────────────────────────
db.questions.insert_many([
    # Python Basics
    {"topic_id": py_basics_id, "question_text": "Which keyword defines a function in Python?", "options": ["func", "define", "def", "function"], "correct_answer": "def"},
    {"topic_id": py_basics_id, "question_text": "What is the output of print(type(3.14))?", "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"], "correct_answer": "<class 'float'>"},
    {"topic_id": py_basics_id, "question_text": "Which of these creates a list in Python?", "options": ["{1,2,3}", "(1,2,3)", "[1,2,3]", "<1,2,3>"], "correct_answer": "[1,2,3]"},
    {"topic_id": py_basics_id, "question_text": "What does len([1,2,3]) return?", "options": ["2", "3", "4", "1"], "correct_answer": "3"},
    {"topic_id": py_basics_id, "question_text": "Which loop is used to iterate over a sequence?", "options": ["while", "loop", "for", "each"], "correct_answer": "for"},

    # Python OOP
    {"topic_id": py_oop_id, "question_text": "Which method is the constructor in Python?", "options": ["__start__", "__init__", "__new__", "__create__"], "correct_answer": "__init__"},
    {"topic_id": py_oop_id, "question_text": "What keyword is used to inherit a class?", "options": ["extends", "inherits", "super", "class Child(Parent):"], "correct_answer": "class Child(Parent):"},
    {"topic_id": py_oop_id, "question_text": "What is 'self' in a Python class?", "options": ["A global variable", "Reference to the current instance", "A reserved keyword like 'this'", "The class itself"], "correct_answer": "Reference to the current instance"},
    {"topic_id": py_oop_id, "question_text": "What does @property decorator do?", "options": ["Marks a method as static", "Allows method to be accessed like an attribute", "Makes method private", "Overloads an operator"], "correct_answer": "Allows method to be accessed like an attribute"},

    # JS Basics
    {"topic_id": js_basics_id, "question_text": "Which keyword declares a block-scoped constant in JS?", "options": ["var", "let", "const", "static"], "correct_answer": "const"},
    {"topic_id": js_basics_id, "question_text": "What does typeof 'hello' return?", "options": ["string", "String", "text", "char"], "correct_answer": "string"},
    {"topic_id": js_basics_id, "question_text": "Which method adds an element to the end of an array?", "options": ["push()", "append()", "add()", "insert()"], "correct_answer": "push()"},
    {"topic_id": js_basics_id, "question_text": "What is the arrow function syntax?", "options": ["fn =>", "=> fn", "(params) => expression", "function =>"], "correct_answer": "(params) => expression"},

    # JS Async
    {"topic_id": js_async_id, "question_text": "What does async/await simplify?", "options": ["Loops", "Promise handling", "DOM manipulation", "Variable scoping"], "correct_answer": "Promise handling"},
    {"topic_id": js_async_id, "question_text": "What does fetch() return?", "options": ["JSON object", "A Promise", "A string", "undefined"], "correct_answer": "A Promise"},
    {"topic_id": js_async_id, "question_text": "Which block catches errors in async/await?", "options": ["finally", "catch", "try-catch", "error"], "correct_answer": "try-catch"},

    # SQL Basics
    {"topic_id": sql_basics_id, "question_text": "Which SQL statement retrieves data?", "options": ["GET", "FETCH", "SELECT", "READ"], "correct_answer": "SELECT"},
    {"topic_id": sql_basics_id, "question_text": "Which clause filters rows in SQL?", "options": ["HAVING", "WHERE", "FILTER", "LIMIT"], "correct_answer": "WHERE"},
    {"topic_id": sql_basics_id, "question_text": "What does COUNT(*) do?", "options": ["Sums values", "Counts non-null rows", "Counts all rows including NULLs", "Returns max value"], "correct_answer": "Counts all rows including NULLs"},

    # SQL Joins
    {"topic_id": sql_joins_id, "question_text": "Which JOIN returns only matching rows from both tables?", "options": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL JOIN"], "correct_answer": "INNER JOIN"},
    {"topic_id": sql_joins_id, "question_text": "LEFT JOIN returns…", "options": ["Only left table rows", "All left rows + matching right rows", "Only matching rows", "All rows from both tables"], "correct_answer": "All left rows + matching right rows"},
    {"topic_id": sql_joins_id, "question_text": "What keyword links tables in a JOIN?", "options": ["USING", "ON", "WITH", "BY"], "correct_answer": "ON"},
])
print("✓ Questions seeded")

# ── Sample Progress ───────────────────────────────────────────────
db.progress.insert_many([
    {"user_id": user1_id, "topic_id": py_basics_id,  "score": 80.0, "correct": 4, "total": 5, "attempt_date": datetime.utcnow()},
    {"user_id": user1_id, "topic_id": js_basics_id,  "score": 75.0, "correct": 3, "total": 4, "attempt_date": datetime.utcnow()},
    {"user_id": user1_id, "topic_id": sql_basics_id, "score": 66.7, "correct": 2, "total": 3, "attempt_date": datetime.utcnow()},
    {"user_id": admin_id, "topic_id": py_oop_id,     "score": 100.0,"correct": 4, "total": 4, "attempt_date": datetime.utcnow()},
])
print("✓ Progress seeded")

print("\n🎉 Seed complete!")
print("Admin login  → admin@learnquiz.com / admin123")
print("User login   → alice@example.com   / alice123")
print("User login   → bob@example.com     / bob123")
