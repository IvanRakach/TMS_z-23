# 1. Сделать класс
# 2. Сделать класс наследник
# 3. Переопределить метод родителя
# 4. Перегрузить метод __ini__


class Person:
    """class for determining persons"""
    def __init__(self, gender, name, age):
        """initiating attributes for persons"""
        self.gender = gender
        self.name = name
        self.age = age

    def show_person(self):
        """show all parameters of our person"""
        print(f"Class 'Person': gender: {self.gender}; name: {self.name}; age: {str(self.age)}")


person_1 = Person('Male', 'Ivan', 28)
# person_1.show_person()
