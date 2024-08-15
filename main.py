# Задача 1
print(f"Задача 1 \n{(9 ** 0.5) * 5}")  # Предполагаемый результат: 15.0

# Задача 2
print(f"Задача 2 \n{9.99 > 9.98 and 1000 != 1000.1}")  # Предполагаемый результат: True

# Задача 3
result_without_priority = 2 * 2 + 2
result_with_priority = 2 * (2 + 2)
print(f"Задача 3 \n{result_without_priority}")  # Предполагаемый результат: 6
print(result_with_priority)     # Предполагаемый результат: 8
print(result_without_priority == result_with_priority)  # Предполагаемый результат: False

# Задача 4
number_str = '123.456'
number_float = float(number_str)
shifted_number = number_float * 10
first_digit_after_decimal = int(shifted_number) % 10
print(f"Задача 4 \n{first_digit_after_decimal}")  # Предполагаемый результат: 4