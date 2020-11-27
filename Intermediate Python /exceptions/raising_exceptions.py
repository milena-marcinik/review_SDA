"""
In Python programming, exceptions are raised when errors occur at runtime. We can also manually raise exceptions using
the raise keyword.


https://www.programiz.com/python-programming/exception-handling
"""

# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#         raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)

a = 3
b = [1, 0, 2]
for elem in b:
    if elem == 0:
        raise ValueError("The divisor cannot be zero")
    result = a / elem
    print(f"Result: {result}")