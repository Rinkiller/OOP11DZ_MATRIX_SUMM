# создать класс моя строка
# доступны все возможноти str
# кроме этого хранится информация о авторе строки(имя) и дата создания
import datetime


class My_str(str):
    """ класс моя строка
        доступны все возможноти str
        кроме этого хранится информация о авторе строки(имя) и дата создания"""

    
    def __new__(cls , string:str , name:str ):
        """ создаем объект класса и наполняем значениями"""
        instance = super().__new__(cls , string)
        instance.name = name
        instance._date = datetime.datetime.now()
        return instance

    
my_str1 = My_str('string №1' , 'Rin')
my_str2 = My_str('string №2' , 'Rin')
print(my_str1)
print(my_str2)
print(my_str1 + my_str2)
print(my_str1._date)
print(my_str1.name)
help(My_str)
print(My_str.__doc__)