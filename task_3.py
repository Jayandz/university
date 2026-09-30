import math
from math import *
#Эксперимент A. int и арифметические операторы
x = 17
y = 5

print(x + y, type(x + y))
print(x - y, type(x - y))
print(x * y, type(x * y))
print(x / y, type(x / y))
print(x // y, type(x // y))
print(x % y, type(x % y))
print(x ** y, type(x ** y))

#Эксперимент B. Большие целые числа
print(2 ** 1000)

#Эксперимент C. float
result = 0.1 + 0.2
print(result, result == 0.3, result - 0.3, math.isclose(result, 0.3))

#Эксперимент D. bool, complex и явное преобразование типов
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(2026), type(str(2026)))
print(bool(0), type(bool(0)))
print(bool(-1), type(bool(-1)))
print(bool(""), type(bool("")))
print(bool("False"), type(bool("False")))

c = complex(2, -3)
print(c, type(c))
print(c.real, c.imag)