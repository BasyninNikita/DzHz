a = input('Введите массив\n')
squares = list()


def form(stroka):
    b = list()
    for i in stroka.split():
        b.append(int(i))
    b.sort()
    # squares = list()
    for i in range(1, int((2 * b[len(b)-1] - 1) ** 0.5) + 1):
        squares.append(i ** 2)
    matr = [[1 if i + j in squares and i != j else 0 for j in b] for i in b]
    print(b)
    print(squares)
    print(len(b))
    for i in range (len(b) ):
        print(matr [i])
    return matr

form(a)
