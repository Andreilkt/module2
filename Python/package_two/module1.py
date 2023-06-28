# Импорт класса User из модуля module

from ..package_one.module import User
#from Python.package_one.module import User



class user_info(User):

    pass

# Новый объект Person из класса Person)
person1 = User("Andrey", 20)

# Вызвать методы
person1.greet()
person1.birth_year()


