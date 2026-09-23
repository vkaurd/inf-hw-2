#Merge Two Sorted Arrays
file = open(r'c:\Users\user\Downloads\rosalind_mer.txt', 'r')
n = int(file.readline().strip()) # длина первого массива
str_A = file.readline().strip().split() # читаем первый массив и превращаем в список целых чисел, сначала strip тк работаем со свей строкой
A = []
for x in str_A:
    A.append(int(x))
m = int(file.readline().strip()) # длина второго массива
str_B = file.readline().strip().split() # читаем второй массив и превращаем в список целых чисел
B = []
for x in str_B:
    B.append(int(x))
file.close()
C = A + B # склеиваем два списка в один общий список с
C.sort()
'''
n = len(C)
for i in range(n): # сколько раз проходимся по списку
    for j in range(0, n - 1): # по элементам (n - 1) тк J+1 выходит за список
        if C[j] > C[j+1]:
            C[j], C[j+1] = C[j+1], C[j] '''
for num in C:
    print(num, end=" ")
