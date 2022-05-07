# 3. Переопределить метод родителя

from task_1 import *


class Student(Person):
    """class for determining students"""
    def __init__(self, gender, name, age, group_number):
        """initiating attributes for student"""
        super().__init__(gender, name, age)
        self.group_number = group_number
        self.__python_lang_knowledge = 1

    def upgrade_python_lang_knowledge(self):
        """upgrading python_lang_knowledge"""
        self.__python_lang_knowledge += 1
        print(f"Python language knowledge has been increased to {self.__python_lang_knowledge} level")

    def show_person(self):
        """
        - show all parameters of our student
        - overriding parent class method "show_person"
        """
        print(f"Class 'Student': gender: {self.gender}; name: {self.name}; age: {str(self.age)}; "
              f"group_number: {str(self.group_number)}; python_lang_knowledge: {self.__python_lang_knowledge}")


person_1 = Person('Male', 'Ivan', 28)
person_2 = Person("Female", "Katya", 27)
person_1.show_person()
person_2.show_person()

student_1 = Student("Male", "Ivan", 28, "z-23")
student_2 = Student("Female", "Katya", 27, "z-23")
student_1.show_person()
student_2.show_person()

student_1.upgrade_python_lang_knowledge()
student_2.upgrade_python_lang_knowledge()
student_1.show_person()
student_2.show_person()
