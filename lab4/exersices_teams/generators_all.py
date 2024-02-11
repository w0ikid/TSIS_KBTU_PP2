# 1
def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

# 2
def even_numbers(n):
    return (i for i in range(n + 1) if i % 2 == 0)

# 3
def div_by_3_and_4(n):
    return (i for i in range(n + 1) if i % 3 == 0 and i % 4 == 0)

# 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

generator = squares(3, 5)

for value in generator:
    print(value)
