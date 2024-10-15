# Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Student Class inheriting from Person
class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")


# Example usage
student = Student("Bentech", "23", "information technology")
student.displayStudent()
