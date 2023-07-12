# создайте класс архив, который хранит пару совйств. Число и строку
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков aрхивов
# list aрхивы также являются свойствами экзампляра

class Arhivary:
    """класс архив, который хранит пару совйств. Число и строку 
        При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков aрхивов
        list aрхивы также являются свойствами экзампляра"""
    _instanse = None
    _list_of_nums_and_strigs = []

    def __new__(cls , number:int = 0 , string:str = '') -> object:
        """При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков aрхивов"""
        instance = super().__new__(cls)
        if cls._instanse:
            cls._list_of_nums_and_strigs.append(cls._instanse)
        cls._instanse = instance
        instance._list_of_nums_and_strigs = cls._list_of_nums_and_strigs.copy()
        return cls._instanse
    
    def __init__(self, number:int = 0 , string:str = '') -> None:
        """создаем экземпляр класса инаполняем его значениями Число и строка"""
        self.number = number
        self.string = string

    def __repr__(self) ->str:
        """вывод данных о содержимом экземпляра класса"""
        return f'{self.number}  {self.string}'   

arc1 = Arhivary(10 , 'xcfhf')
print(arc1)
print(arc1._list_of_nums_and_strigs)
arc2 = Arhivary(20 , ' vRGGGDVDEHEHe')
print(arc2)
print(arc2._list_of_nums_and_strigs)
arc3 = Arhivary(30 , ' vxfngnRr')
print(arc3)
print(arc3._list_of_nums_and_strigs)
arc4 = Arhivary(10 , ' vjxdgfbxdfhrbd')
print(arc4)
print(arc4._list_of_nums_and_strigs)
