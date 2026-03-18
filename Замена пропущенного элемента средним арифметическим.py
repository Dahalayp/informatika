numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Суммируем все элементы, кроме None
total = sum(x for x in numbers if x is not None)
# Общее количество элементов (включая пропуск)
count = len(numbers)

# Вычисляем среднее арифметическое
mean = total / count

# Заменяем None на полученное среднее
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = mean
        break

# Выводим результат
print("Измененный список:", numbers)

