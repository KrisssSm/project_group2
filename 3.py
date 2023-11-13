# Вводим целые числа n и k 
n, k = map(int, input().split())

# Вводим n целых чисел, каждое с новой строки
numbers = [int(input()) for _ in range(n)]

# Для k первых элементов найдем и выведем:
k_numbers = numbers[:k]  # выбираем только первые k элементов

# Среднее арифметическое
average_arithmetic = sum(k_numbers) / k

# Среднее гармоническое
average_harmonic = k / sum(1/x for x in k_numbers)

# Максимальный элемент
max_element = max(k_numbers)

# Второй максимальный элемент
second_max_element = sorted(k_numbers)[-2]

# Минимальный элемент
min_element = min(k_numbers)
