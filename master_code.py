def QuestionsMarks(str):
    ultimo = []
    i = 0
    while i < len(str):
        a = str[i]
        if isinstance(a, int):
            ultimo.append([a, i])
            i += 1
        else:
            i += 1
    return ultimo


######transform the list into int and strings.
def is_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return s


# returns a list with index sum 10
def soma(lista):
    ind = []
    i = 0
    while i < len(lista) - 1:
        first = lista[i]
        second = lista[i + 1]
        if first[0] + second[0] == 10:
            ind.append([first[1], second[1]])
            i += 1
        else:
            i += 1
    return ind


def questionmark(position, vector):
    i = 0
    while (i < len(position) and True):
        range = position[i]
        initial = range[0]
        final = range[1]
        contador = 0
        while initial<final:
            if vector[initial] == '?':
                contador += 1
                initial += 1
            else:
                initial += 1

        if not (contador == 3):
            return False
        else:
            return True
            i += 1

    if i==len(position):
        return True
    else:
        return False


stringa = tuple(input("Yup?"))
lista = list(stringa)
final = list(map(is_number, lista))
print(questionmark(soma(QuestionsMarks(final)), stringa))
