# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    # the portion that can cause an exception is placed inside the try block
    try:
        print("The entry is", entry)
        r = 1 / int(entry)
        break
    except:
        # print the name of the exception using the exc_info() function inside sys module
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()

print("The reciprocal of", entry, "is", r)
