from random import sample
import string


def get_random_password(length = 8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    population = string.digits + string.ascii_uppercase + string.ascii_lowercase
    password = sample(population, k = length)
    return "".join(password)


print(get_random_password())
