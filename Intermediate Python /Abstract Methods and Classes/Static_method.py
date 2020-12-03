"""
The @staticmethod Decorator

The @staticmethod decorator is similar to @classmethod in that it can be called from an uninstantiated class object,
although in this case there is no cls parameter passed to its method.

https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/
"""


class Student(object):

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1


Student.is_full_name('Scott Robinson')   # True
Student.is_full_name('Scott')            # False
