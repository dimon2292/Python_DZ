from random import randint
def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    list_ = []
    while len(list_) != 15:
        i = randint(-10, 10)
        if i not in list_:
                list_.append(i)

    return list_
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
