import random
import os
import time

def print_matrix (m):                                                                                                   # функция вывода матрицы
    for i in m:
        for j in i:
            print ('%4d' %j, end= ' ')
        print()
try:
    start = time.time()
    n = int(input())
    while n < 6:
        n = int(input('Введите количество строк(столбцов) квадратной матрицы > 5'))
    k = int(input())
    A = [[0 for i in range (n)]for j in range (n)]                                                                      # задаем матрицу A
    F = [[0 for i in range(n)] for j in range(n)]                                                                       # задаем матрицу F
    for i in range (n):
        for j in range (n):
            A[i][j] = random.randint(-10,10)
            F[i][j] = A[i][j]
    print ('A')
    print_matrix(A)
    s = 0                                                                                                               # введем переменную для подсчета количество нулей в C в нечетных столбцах в области 1
    r = 1                                                                                                               # введем переменную для подсчета произведения чисел по периметру области 4
    for i in range(n):
        for j in range(n):
            if i < (n // 2) and j > (n // 2 - (n - 1) % 2):
                if j < (n - i - 1) and j < (n // 2 + i + n % 2) and j % 2 == 0 and A[i][j] == 0:
                    s += 1
                if i > n // 4 and ((n - 1 - i) < j < (n // 2 + i + n % 2)) and (
                        j == (n - i) or i == (n // 2 - 1) or j == (n // 2 + i - (n - 1) % 2)):
                    r *= A[i][j]
    print (s,r)
    if s > r:
        for i in range(n // 2 + 1):                                                                                     # если нулей больше то мы симметрично меняем область 1 и 3
            for j in range(n):
                if i < n // 2 and j > (n // 2 - (n - 1) % 2) and j < (n - i - 1) and j < (n // 2 + i + n % 2):
                    F[i][j], F[i][n - j - n // 2 - (n - 1) % 2 - 1] = F[i][n - j - n // 2 - (n - 1) % 2 - 1], F[i][j]
    else:                                                                                                               # иначе меняем B и E местами несимметрично
        for i in range(n // 2 + 1):
            for j in range(n // 2 + 1):
                if j < n // 2 and i < n // 2:
                    F[i][j], F[i + n // 2 + n % 2][j + n // 2 + n % 2] = F[i + n // 2 + n % 2][j + n // 2 + n % 2],F[i][j]
    print('F')
    print_matrix(F)
    At = [[0 for i in range(n)] for j in range(n)]                                                                      # траснпонируем матрицу A
    for i in range(n):
        for j in range(i, n):
            At[i][j], At[j][i] = A[j][i], A[i][j]
    print('At')
    print_matrix(At)
    At = [[j * k for j in i] for i in At]
    print('At*K')
    print_matrix(At)
    Summa = [[0 for i in range(n)] for j in range(n)]                                                                   # вычисляем сумму матрицы A и F
    for i in range(n):
        for j in range(n):
            Summa[i][j] += F[i][j]+A[i][j]
    print('Summa')
    print_matrix(Summa)
    Vichitanie = [[0 for i in range(n)] for j in range(n)]                                                              # находим разность суммы и матрицы F
    for i in range(n):
        for j in range(n):
            Vichitanie[i][j] += Summa[i][j]-F[i][j]
    print('Vichitanie')
    print_matrix(Vichitanie)
    Result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            Result[i][j] = sum([At[i][h] * Vichitanie[h][j] for h in range(n)])
    print('Result')
    print_matrix(Result)
    print(f"\nВремя выполнения {time.time() - start} секунд")
except ValueError:
    print("Введённые данные не являются числом")
