a = input('Введите массив\n')
squares = list()


def form(stroka):
    b = list()
    for i in stroka.split():
        b.append(int(i))
    b.sort(reverse=1)
    # squares = list()
    for i in range(1, int((2 * b[0] - 1) ** 0.5) + 1):
        squares.append(i ** 2)
    matr = [[0 for i in range(len(b) + 1)] for j in range(len(b))]

    print(b)
    print(squares)
    print(len(b))
    print(matr)


form(a)
