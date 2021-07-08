def fizz_buzz(n: int):
    fizz_buzz_list = []

    for i in range(1, n+1):
        fizz_buzz_list.append(value_generate(i))

    return fizz_buzz_list


def value_generate(index: int):
    item = ''
    if index % 3 == 0 and index % 5 == 0:
        item = "FizzBuzz"
    elif index % 3 == 0:
        item = "Fizz"
    elif index % 5 == 0:
        item = "Buzz"
    else:
        item = str(index)
    return item
