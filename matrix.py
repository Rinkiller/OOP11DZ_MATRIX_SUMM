"""маин Урок 11. ООП. Особенности Python"""
# Урок 11. ООП. Особенности Python
# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


class Matrix(list):
    """ Класс матрица хранит внутри себя прямоугольную матрицу целочисленных значений
        И позволяет проводить арифметические операции с данными матрицами
        Такие как сложение , вычитание , умножение матриц одна на другую
        А также провеодить операции сравнения матриц"""
    matrix: list[list[int]]

    def __new__(cls, matrix: list[list[int]]) -> object:
        """Генератор объекта класса"""
        instance = super().__new__(cls)
        instance.matrix = matrix
        return instance

    def __init__(self, matrix: list[list[int]]) -> None:
        """Инициализация матрицы"""
        self.matrix = matrix
        super().__init__(self)

    def __str__(self) -> str:
        """Строковое представление матрицы
        Выводит прямоугольное представление марицы
        автоматически добавляя перенос на новую строку в конце каждой строки """
        rezult_str = ''
        for line in self.matrix:
            rezult_str = rezult_str + str(line) + '\n'
        return rezult_str[:-1]


# Равенство
# Две матрицы равны, если они имеют одинаковое число строк и столбцов и соответствующие элементы равны
# Другими словами, A = B, если мы имеем aij = bij для всех i и j.

    def __eq__(self, other: object) -> bool:
        """Равенство. Две матрицы равны, если они имеют одинаковое число строк и столбцов и соответствующие элементы равны"""
        if len(self.matrix) != len(other.matrix):
            return False
        for index, _ in enumerate(self.matrix):
            if len(self.matrix[index]) != len(other.matrix[index]):
                return False
            for el_index , _ in enumerate(self.matrix[index]):
                if self.matrix[index][el_index] != other.matrix[index][el_index]:
                    return False
        return True


# Определения наибольшей из двух матриц нет при условии равности кол-ва столбцов и колонок
# принято решение сравнивать среднее арифметическое всех элементов обоих матриц


    def __gt__(self, other: object) -> bool:
        srednee_self = sum(sum(line) for line in self.matrix)/len(sum(self.matrix, []))
        srednee_other = sum(sum(line) for line in other.matrix)/len(sum(other.matrix, []))
        return srednee_self > srednee_other


# Операция сложения двух матриц может применяться,
# если матрицы имеют одинаковое число столбцов и строк. Сложение записывают как C = A + B.
# В этом случае полученная в результате матрица C имеет тот же самый номер строк и столбцов, как A или B.
# Каждый элемент C — сумма двух соответствующих элементов A и B: aij + bij.

    def __add__(self, other: object) -> object:
        """метод производит сложение двух матриц. Результатом является новая матрица"""
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        else:
            for index , _ in enumerate(self.matrix):
                if len(self.matrix[index]) != len(other.matrix[index]):
                    raise ValueError
        new_matrix = []
        for index , _ in enumerate(self.matrix):
            line = []
            for ind_el , _ in enumerate(self.matrix[index]):
                line.append(self.matrix[index][ind_el] +
                            other.matrix[index][ind_el])
            new_matrix.append(line)
        return Matrix(new_matrix)

# Операция вычитания производится аналогично сложению,
# за исключением того, что каждый элемент B вычитается из соответствующего элемента A: dij= aij – bij.
    
    
    def __sub__(self, other: object) -> object:
        """метод производит вычитание двух матриц. Результатом является новая матрица"""
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        else:
            for index in range(len(self.matrix)):
                if len(self.matrix[index]) != len(other.matrix[index]):
                    raise ValueError
        new_matrix = []
        for index in range(len(self.matrix)):
            line = []
            for ind_el in range(len(self.matrix[index])):
                line.append(self.matrix[index][ind_el] -
                            other.matrix[index][ind_el])
            new_matrix.append(line)
        return Matrix(new_matrix)

# Две матрицы различного размера могут быть перемножены, если число столбцов первой матрицы совпадает с числом строк второй матрицы.
# Если A — матрица размера l x m, а матрица B размера m x p, то произведением будет матрица C размером l x p.
# Если элемент матрицы A обозначить aij, а каждый элемент матрицы B обозначить bjk,
# то элемент матрицы C — cik — вычисляется следующим образом: cik = EaijХbjk
    
    
    def __mul__(self, other: object) -> object:
        """метод позволяет премножать одну матрицу на другую"""
        for index , _ in enumerate(self.matrix):
            if len(other.matrix) != len(self.matrix[index]):
                raise ValueError
        result_matrix = [[0 for x in range(len(other.matrix[0]))] for y in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j] 
        return Matrix(result_matrix)

print('первая матрица')
matr1 = Matrix([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(matr1)
print('вторая матрица')
matr2 = Matrix([[1, 1, 1],
                [2, 2, 2],
                [3, 3, 3]])
print(matr2)
print('сложение матриц')
matr3 = matr1 + matr2
print(matr3)
print('вычитание матриц')
matr4 = matr1 - matr2
print(matr4)






print('сравнение матриц matr11 == matr1')
matr11 = matr1
print(matr11 == matr1)
print('сравнение матриц matr1 == matr2')
print(matr1 == matr2)

print('сравнение матриц matr1 > matr2')
print(matr1 > matr2)

matr5 = Matrix([[1, 2],
                [2, 3],
                [4, 5],
                [1, 2]])

matr6 = Matrix([[1, 3, 4],
                [4, 5, 6]])
# матрицы matr5 и matr6 могут быть перемножены т.к. число столбцов первой равно числу строк второй

print('перемножение матриц')
print(matr5 * matr6)

help(Matrix)

