# Создаем список из 6 строк
lines = [
    "картошка",
    "банан",
    "баран",
    "чайник",
    "барсук",
    "мультиварка"
]

# Переменная для подсчета строк с буквой 'б'
count = 0

# Используем цикл для подсчета строк, содержащих букву 'б'
for line in lines:
    if 'б' in line.lower():  # Приводим к нижнему регистру для учета заглавной буквы
        count += 1

# Выводим результат
print(f"Количество строк, содержащих букву 'б': {count}")

