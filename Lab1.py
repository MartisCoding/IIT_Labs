
def iterate():
    print(*range(1, int(input("Введите число: ")) + 1), sep="\n")

def find_max():
    print(f"Большее число: {max(int(input('Введите первое число: ')), int(input('Введите второе число:')))}")
find_max()
