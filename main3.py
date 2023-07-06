# Создайте функцию генератор чисел Фибоначчи

def generator_fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in generator_fib(10):
    print(i)
