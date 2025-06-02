from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x ** 2, numbers))
print("Квадрати:", squares)


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Парні числа:", even_numbers)

product = reduce(lambda x, y: x * y, numbers)
print("Добуток:", product)