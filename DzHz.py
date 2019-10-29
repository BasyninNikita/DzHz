a = input('Введите массив\n')
squares = set()


# Функция form из исходной строки с числами заданного массива
# формирует матрицу смежности являющуюся входными данными
# для задачи поиска гамильтонова пути
def form(stroka):
    b = list()
    for i in stroka.split():
        b.append(int(i))
    b.sort()
    # squares = list()
    squares = {i ** 2 for i in range(1, int((2 * b[len(b) - 1] - 1) ** 0.5) + 1)}
    matr = [[1 if i + j in squares and i != j else 0 for j in b] for i in b]
    print(b)
    print(squares)
    print(len(b))
    for i in range(len(b)):
        print(matr[i])
    return matr


form(a)
