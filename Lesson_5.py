def is_number_simple(number):
    if all([number % i for i in range(2, int(number ** 0.5) + 1)]):
        print("Number " + str(number) + " is simple")
    else:
        print("Number " + str(number) + " is not simple")


def simple_dividers(number):
    dividers = []
    count = 2
    while count <= number:
        if number % count == 0:
            dividers.append(count)

        count += 1
    return dividers


def max_divider(number):
    d = 2
    last_d = 0
    while d * d <= number:
        if number % d == 0:
            number //= d
        else:
            d += 1
    print(number)


def use_dividers(number):
    dividers = []
    count = 2
    while count * count <= number:
        if number % count == 0:
            dividers.append(count)
            number //= count
        else:
            count += 1
    if number > 1:
        dividers.append(number)
    return dividers


def max_any_dividers(number):
    if len(simple_dividers(number))> 1:
        return max(simple_dividers(number))
    else:
        return number


num = int(input('Input number: '))
is_number_simple(num)
print(simple_dividers(num))
max_divider(num)
print(use_dividers(num))
print(max_any_dividers(num))
