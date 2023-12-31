def armstrong_numbers(k):
    armstrong_nums = []  # Создаем пустой список для хранения чисел Армстронга

    for num in range(1, k + 1):  # Итерируем через все числа от 1 до k
        num_str = str(num)  # Преобразуем число в строку
        n = len(num_str)  # Находим количество цифр в числе
        sum_of_digits = sum(int(digit)**n for digit in num_str)  # Вычисляем сумму цифр числа, возведенных в степень количества цифр

        if sum_of_digits == num:  # Проверяем, является ли число числом Армстронга
            armstrong_nums.append(num)  # Если да, добавляем его в список

    return armstrong_nums  # Возвращаем список чисел Армстронга
k = 1000
result = armstrong_numbers(k)
print(result)  # Выводим результат
