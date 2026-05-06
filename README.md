# 📚 LearnQuiz — Learning & Quiz Platform

A full-stack web application for learning programming languages and testing knowledge through quizzes. Built with **React**, **Flask**, and **MongoDB**.

---

## 🗂 Project Structure

```
learnquiz/
├── server/                  # Flask backend
│   ├── app.py               # Application factory & entry point
│   ├── seed.py              # Database seed script
│   ├── requirements.txt
│   ├── .env.example
│   ├── models/
│   │   └── db.py            # MongoDB connection
│   └── routes/
│       ├── auth.py          # Register / Login
│       ├── user.py          # User-facing API
│       └── admin.py         # Admin CRUD + Analytics
│
└── client/                  # React frontend
    ├── public/
    │   └── index.html
    ├── package.json
    ├── .env.example
    └── src/
        ├── index.js
        ├── index.css
        ├── App.js
        ├── api/
        │   └── axios.js         # Axios instance + interceptors
        ├── context/
        │   └── AuthContext.js   # JWT auth context
        ├── components/
        │   ├── Shared.js        # Spinner, Alert, ProtectedRoute
        │   └── Sidebar.js       # Navigation sidebar
        └── pages/
            ├── AuthPages.js         # Login & Register
            ├── UserPages.js         # Dashboard, Languages, Topics, Quiz, Progress
            ├── AdminAnalyticsPage.js# Analytics dashboard
            └── AdminCrudPages.js    # Admin CRUD: Languages, Topics, Questions, Users
```

---

## 🚀 Setup & Running

### Prerequisites
- Python 3.9+
- Node.js 18+
- MongoDB running locally (or a MongoDB Atlas URI)

---

### 1. MongoDB Setup

Make sure MongoDB is running on `localhost:27017` (default).

You can also use MongoDB Atlas — just update `MONGO_URI` in your `.env`.

---

### 2. Backend (Flask)

```bash
cd server

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env — set MONGO_URI and JWT_SECRET_KEY

# Seed the database with sample data
python seed.py

# Start the Flask server
python app.py
```

The API will be available at **http://localhost:5000**

---

### 3. Frontend (React)

```bash
cd client

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# REACT_APP_API_URL=http://localhost:5000/api  (default, no change needed)

# Start the React dev server
npm start
```

The app will open at **http://localhost:3000**

---

## 🔐 Demo Credentials

After running `seed.py`:

| Role  | Email                    | Password   |
|-------|--------------------------|------------|
| Admin | admin@learnquiz.com      | admin123   |
| User  | alice@example.com        | alice123   |
| User  | bob@example.com          | bob123     |

---

## 📡 API Reference

### Auth
| Method | Endpoint         | Auth | Description        |
|--------|-----------------|------|--------------------|
| POST   | /api/register   | —    | Register new user  |
| POST   | /api/login      | —    | Login, get JWT     |

### User
| Method | Endpoint                    | Auth | Description               |
|--------|-----------------------------|------|---------------------------|
| GET    | /api/languages              | JWT  | List all languages        |
| GET    | /api/topics/:language_id    | JWT  | Topics for a language     |
| GET    | /api/questions/:topic_id    | JWT  | Questions for a topic     |
| POST   | /api/submit-quiz            | JWT  | Submit quiz, get score    |
| GET    | /api/progress               | JWT  | Current user's progress   |

### Admin
| Method | Endpoint                       | Auth        | Description              |
|--------|-------------------------------|-------------|--------------------------|
| GET    | /api/admin/analytics          | JWT (admin) | Platform analytics       |
| GET    | /api/admin/users              | JWT (admin) | All users list           |
| POST   | /api/admin/language           | JWT (admin) | Create language          |
| PUT    | /api/admin/language/:id       | JWT (admin) | Update language          |
| DELETE | /api/admin/language/:id       | JWT (admin) | Delete language + cascade|
| POST   | /api/admin/topic              | JWT (admin) | Create topic             |
| PUT    | /api/admin/topic/:id          | JWT (admin) | Update topic             |
| DELETE | /api/admin/topic/:id          | JWT (admin) | Delete topic + questions |
| POST   | /api/admin/question           | JWT (admin) | Create question          |
| PUT    | /api/admin/question/:id       | JWT (admin) | Update question          |
| DELETE | /api/admin/question/:id       | JWT (admin) | Delete question          |
| GET    | /api/admin/questions/:topicId | JWT (admin) | All questions (w/ answers)|

---

## 🗄 Database Collections

### users
```json
{
  "_id": "ObjectId",
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "password": "<bcrypt hash>",
  "role": "user | admin",
  "last_login": "2026-04-08T09:00:00Z",
  "login_count": 3,
  "created_at": "2026-01-01T00:00:00Z"
}
```

### languages
```json
{ "_id": "ObjectId", "language_name": "Python", "description": "..." }
```

### topics
```json
{ "_id": "ObjectId", "language_id": "ObjectId", "topic_name": "Python Basics", "content": "..." }
```

### questions
```json
{
  "_id": "ObjectId",
  "topic_id": "ObjectId",
  "question_text": "Which keyword defines a function?",
  "options": ["def", "func", "function", "define"],
  "correct_answer": "def"
}
```

### progress
```json
{
  "_id": "ObjectId",
  "user_id": "ObjectId",
  "topic_id": "ObjectId",
  "score": 80.0,
  "correct": 4,
  "total": 5,
  "attempt_date": "2026-04-08T09:00:00Z"
}
```

---

## ✨ Features

### User Features
- Register and login with JWT authentication
- Browse programming languages
- Read topic content (markdown-rendered)
- Take quizzes with a question navigator
- View score, answer review, and full progress history

### Admin Features
- **Analytics Dashboard** — Total users, total logins, tests taken, active users, per-user table
- **Manage Languages** — Add, edit, delete (with cascade)
- **Manage Topics** — Add, edit, delete per language
- **Manage Questions** — Add, edit, delete per topic; correct answer highlighted
- **Users List** — View all users with login stats

---

## 🛡 Security

- Passwords hashed with **bcrypt**
- All protected routes require a valid JWT (Bearer token)
- Admin routes additionally verify `role == "admin"` server-side
- CORS configured for localhost development
