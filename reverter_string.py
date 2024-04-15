string_example: str = 'subi no onibus'


def reverse_string(string: str) -> str:
    lista = list(string)
    new = ''

    i = -1
    for _ in range(len(lista)):
        new += lista[i]
        i = i - 1
    return new


print(reverse_string(string_example))
