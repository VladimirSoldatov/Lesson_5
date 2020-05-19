def round_function(in_num, ch):
    temp_one = ('{:.' + str(ch) + 'f}').format(in_num)

    return temp_one


def ticket(number):
    sum1 = sum2 = 0
    num_temp = number
    for i in range(len(num_temp)):
        if i < len(num_temp) / 2:
            sum1 += int(num_temp[i])
        else:
            sum2 += int(num_temp[i])
    return sum1 == sum2


def fib_function(num):
    if num < 2:
        return 1
    else:
        return fib_function(num - 1) + fib_function(num - 2)


# n = 4 #Прорверка
# if fib(n)*fib(n) == fib(n + 1) * fib(n) - fib(n - 1) * fib(n):
#     print(fib(n))
def custom_sort(in_list):
    for j in range(0, len(in_list)):
        for i in range(0, len(in_list) - 1):
            if in_list[i] > in_list[i + 1]:
                temp = in_list[i]
                in_list[i] = in_list[i + 1]
                in_list[i + 1] = temp
            else:
                continue
    return in_list


# n = [9, 1, 5, 9, 3, 5, 9, 0, 8, 6, 3, 8]
# print(custom_sort(n))

def add():
    print('Добавление выполнено')


def delete():
    print('Удаление выполнено')


def printing():
    print('Печать выполнена')


def execluse():
    print('Счет выполнен')


temp_var = 0
list_action = dict()
list_command = ('Добавить', 'Удалить', 'Распечатать', 'Посчитать', 'Выйти')
while temp_var != 5:
    print('Введите желаемое дейтствие')
    for i, item in enumerate(list_command):
        print(f'{i + 1}. {item}')
        temp_dict = {i + 1: item}
        list_action.update(temp_dict)

    temp_var = int(input())
    select = list_action.get(temp_var)
    if select == 'Добавить':
        add()
    elif select == 'Удалить':
        delete()
    elif select == 'Распечатать':
        printing()
    elif select == 'Посчитать':
        execluse()
    elif select is None:
        print(f'Введено значение {temp_var}, которое не в интервале от 1 до 5')
        print(f'Попробуте еще или введите 5, чтобы завршить программу')

