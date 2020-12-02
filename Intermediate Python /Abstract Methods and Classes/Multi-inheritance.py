class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, salary, number_of_hours):
        super().__init__(name, age)
        self.salary = salary
        self.number_of_hours = number_of_hours

    def show_finance(self):
        return self.salary * self.number_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, salary, number_of_hours, scholarship):
        Employee.__init__(self, name, age, salary, number_of_hours)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.salary * self.number_of_hours + self.scholarship
