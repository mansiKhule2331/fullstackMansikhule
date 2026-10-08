# for i in range(1, 6):
#   for j in range(1, i + 1):
#     print(j, end="")
#   print()
# for i in range(1, 6):
#   for j in range("*", i + 1):
#     print(j, end="")
#   print()
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

# Example usage with 5 rows
inverted_triangle(5)