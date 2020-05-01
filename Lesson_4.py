import random


def f(list_tail, n):
    list_n = []
    for i in range(n):
        list_n.append(list_tail[random.randint(0, len(list_tail) - 1)])
    return list_n


def max_count(list_tail):
    return max(list_tail, key=list_tail.count)


def min_letter(tail_list):
    min_i = []
    for i in tail_list:
        min_i.append(i[0])
    return min(min_i, key=min_i.count)


def open_file(file_name_user):
    with open(file_name_user, "r") as my_file:
        temp = 0
        my_str = str
        for line in my_file:
            time = line.split()[0].replace('-', '') + line.split()[1].replace(':', '').replace(',', '')
            if temp < int(time):
                temp = int(time)
                my_str = line.split()[0] + " " + line.split()[1]
    return my_str


our_list = ("anna", "andrey", "alex", "vladimir", "valeria",
            "valeria", "victor", "galina", "gleb", "gabriel",
            "eva", "evgeniy", "jozepine", "jack", "inna",
            "igor", "konstantin", "kirill", "larisa", "leya",
            "maria", "michael", "natalia", "nathan", "thomas")
new_list = f(our_list, 100)
print(new_list)
print("Самое встречающееся имя - " + max_count(new_list))
print("Самая редкая буква с которой начинается имя - "+ min_letter(new_list))
file_name = "d:\\log"
print("Last data is " + open_file(file_name))
