def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number ** 2

def max_of_two(x, y):
    return max(x, y)


def describe_person(name, age=30):
    return f"Имя: {name} \nВозраст: {age}"

def is_prime(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True
print(is_prime(10))
print(is_prime(7))