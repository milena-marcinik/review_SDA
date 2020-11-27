# The try block will raise an error when trying to write to a read-only file


try:
    file = open("temp.txt")
    file.write("I saw a lion")
except FileNotFoundError:
    print("An error occurred while processing the file!")
finally:
    file.close()


# The program can continue, without leaving the file object open
