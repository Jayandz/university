"""
Программа запрашивает данные о вычислительном эксперименте (исследователь,
название, число запусков, длительность запуска, комплексный коэффициент)
и выводит на экран итоговую информационную карточку.
"""

researcher = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs = int(input("Количество запусков: "))
duration = float(input("Длительность одного запуска (с): "))
coef_real = float(input("Действительная часть коэффициента: "))
coef_imag = float(input("Мнимая часть коэффициента: "))

total_seconds = runs * duration
total_minutes = total_seconds / 60
coefficient = complex(coef_real, coef_imag)
magnitude_squared = coef_real ** 2 + coef_imag ** 2
has_runs = bool(runs)

print("=" * 40)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {researcher}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {magnitude_squared:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)

print(
    f"Типы введенных значений: "
    f"{type(researcher)}, {type(experiment)}, {type(runs)}, "
    f"{type(duration)}, {type(coef_real)}, {type(coef_imag)}"
)