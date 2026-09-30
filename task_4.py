student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

#первый и последний символ имени
print(student[0], student[-1])

#срез с именем и с фамилией
print(student[0:4])
print(student[5:])

#верхний и нижний регистр
print(student.upper())
print(student.lower())

#инициалы через индексацию
i = student[0] + "." + student[5] + "."
print(i)

#название курса в обратном порядке через срез
print(course[::-1])

per = completed / total * 100
result_percent = "%s — %s: %d/%d (%s%%)" % (student, course, completed, total, per)
result_format = "{} — {}: {}/{} ({}%)".format(student, course, completed, total, per)
result_fstring = f"{student} — {course}: {completed}/{total} ({per}%)"

print(result_percent)
print(result_format)
print(result_fstring)

#Исследуйте Unicode:
symbol = "Я"

print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol.encode("utf-8")))

#ошибка
# symbol[0] = 'А'
# print(symbol)