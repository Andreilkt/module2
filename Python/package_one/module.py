# Импортируемый модуль и класс  для импорта User


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Привет, я {self.name}')

    def birth_year(self):
        print(f'Дата рождения {2021 - self.age}')
