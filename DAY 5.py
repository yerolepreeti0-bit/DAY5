def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area, perimeter = calc_rectangle(length, width)

print("Area:", area, "Perimeter:", perimeter)



def power(base, exp):
    return base ** exp


def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)


import math_operators

result_power = math_operators.power(5, 2)

numbers = [10, 20, 30, 40]
result_average = math_operators.average(numbers)

print("5^2 =", result_power)
print("Average =", result_average)