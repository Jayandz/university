a = 1000
b = a
c = None

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print(c is None)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)