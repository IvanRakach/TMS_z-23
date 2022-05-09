class Person:
    """class for determining persons"""
    total_number_of_persons = 0

    def __init__(self, gender, name, age):
        """initiating attributes for persons"""
        self.gender = gender
        self.name = name
        self.age = age
        Person.total_number_of_persons = Person.total_number_of_persons + 1

    def show_person(self):
        """show all parameters of our person"""
        print(f"Class 'Person': gender: {self.gender}; name: {self.name}; age: {str(self.age)}")

    @classmethod
    def total_persons(cls):
        print(f"total_number_of_persons : {cls.total_number_of_persons}")

    @staticmethod
    def find_the_youngest_student(*age):
        print(f"the youngest student: {min(age)}")


class Student(Person):
    """class for determining students"""

    def __init__(self, gender, name, age, group_number):
        """initiating attributes for student"""
        super().__init__(gender, name, age)
        self.group_number = group_number
        self.__python_lang_knowledge = 1
        # Student.total_number_of_students = Student.total_number_of_students + 1

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


# person_1 = Person('Male', 'Ivan', 28)
# person_2 = Person("Female", "Katya", 27)
# person_1.show_person()
# person_2.show_person()

student_1 = Student("Male", "Ivan", 28, "z-23")
student_2 = Student("Female", "Katya", 27, "z-23")
# student_1.show_person()
# student_2.show_person()
#
student_1.upgrade_python_lang_knowledge()
student_2.upgrade_python_lang_knowledge()
# student_1.show_person()
# student_2.show_person()

print("===============================")
print("========= tasks 1 - 3 =========")
print("===============================")
Person.total_persons()
Person.find_the_youngest_student(28, 30)


print("===============================")
print("=========== task 4 ============")
print("===============================")


class Meta(type):
    """
    Metaclass form 'type'
    'cls' - ссылка на созданный класс
    'name' - имя создаваемого класса
    'base' - кортеж базовых классов
    'attrs' - словарь из атрибутов класса
    """
    def __int__(cls, name, base, attrs):  # на этом моменту новый класс уже создан
        cls.__int__ = Meta.create_local_attrs
        cls.class_attr = attrs

    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attr.items():
            self.__dict__[key] = value


class Blog(metaclass=Meta):
    title = "Заголовок"
    content = "Контент"
    photo = "Путь к фото"


pst = Blog()
print(pst.__dict__)
