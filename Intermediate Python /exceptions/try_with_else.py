"""
In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
Exceptions in the else clause are not handled by the preceding except clauses.

https://www.programiz.com/python-programming/exception-handling
"""

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
