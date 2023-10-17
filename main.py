def armstrong_numbers(k):
    armstrong_nums = []

    for num in range(1, k + 1):
        num_str = str(num)
        n = len(num_str)
        sum_of_digits = sum(int(digit)**n for digit in num_str)

        if sum_of_digits == num:
            armstrong_nums.append(num)

    return armstrong_nums
k = 1000
result = armstrong_numbers(k)
print(result)