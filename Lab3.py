
def read_and_print():
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)


def read_and_print2():
    with open('example.txt', 'r') as file:
        for k, line in enumerate(file):
            print(k, line.strip())


def write_information():
    data = input("Введите то, что ходите записать в файл: ")
    with open("user_input.txt", "a+") as file:
        file.writelines(data + "\n")


def read_and_print_with_error_handling(filename:str):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Такого файла несуществует или имя файла введено не корректно.")
read_and_print_with_error_handling("exampel.txt")