import math


def square(number):
    return math.ceil(number * number)


num = float(input("Введите сторону квадрата:"))
print(f"Площадь квадрата:{square(num)}")
