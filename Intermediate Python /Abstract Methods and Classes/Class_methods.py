"""
The @classmethod Decorator

This decorator exists so you can create class methods that are passed the actual class object within the function call,
much like self is passed to any other ordinary instance method in a class.

https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/
"""


# class Student(object):
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
# scott = Student('Scott', 'Robinson')


class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student


scott = Student.from_string('Scott Robinson')
