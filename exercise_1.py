def factorial(number):
    if number == 0:
        return 1
    return factorial(number - 1) * number


n = int(input("Введите натуральное целое число: "))

factorials = list()

for i in range(factorial(n), 0, -1):
    factorials.append(factorial(i))

print(factorials)
