#Majority Element
file = open(r'c:\Users\user\Downloads\rosalind_maj (1).txt', 'r')
first_line = file.readline().strip() # читаем первую строчку (там параметры k и n) и убираем невид символы
parts = first_line.split()
k = int(parts[0]) # кол-во массивов
n = int(parts[1]) # длина каждого массива
answers = []
for i in range(k):
    line = file.readline().strip() # читаем след строчку(массив)
    str_numbers = line.split() # превращаем строчку в список целых чисел
    numbers = []
    for x in str_numbers:
        numbers.append(int(x))
    found = False # заводим флаг, нашли ли лидера. изначально — False
    unique_numbers = set(numbers) # убираем повторения, чтобы работать с числом только 1 раз
    for num in unique_numbers:  # проверяем каждое уникальное число
        count_num = numbers.count(num) # сколько раз это число встречается в исходном списке numbers, без set()
        if count_num > (n / 2):
            answers.append(num) # добавляем это число в наш список ответов
            found = True        # лидер найден
            break               # прерываем внутренний цикл для этого массива
    if found == False:
        answers.append(-1) # Добавляем -1 в ответы
file.close()
for ans in answers:
    print(ans, end=" ") #end для для пробела, курсор остается на той же строчке