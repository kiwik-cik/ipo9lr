import math
def circle_area(r):
    return math.pi * r ** 2
def triangle_area(b, h):
    return 0.5 * b * h
def armstrong_numbers(k):
    armstrong_nums = []

    for num in range(1, k + 1):
        num_str = str(num)
        n = len(num_str)
        sum_of_digits = sum(int(digit)**n for digit in num_str)

        if sum_of_digits == num:
            armstrong_nums.append(num)

    return armstrong_nums
import sys
sys.path
import custom_functions
k = 1000
result = custom_functions.armstrong_numbers(k)
print(result)