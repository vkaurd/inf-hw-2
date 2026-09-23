#Computing GC content 1
file = open(r'c:\Users\user\Downloads\rosalind_gc.txt', 'r')
lines = file.readlines()
file.close()
dna_dict = {} # создаем словарь для хранения ДНК. тк есть ID и значения
current_id = "" # ключ — ID (Rosalind_xxxx), значение — собранная строка ДНК
# проходимся по строкам файла и склеиваем ДНК
for line in lines:
    line = line.strip() # удаляем невидимые символы переноса строки (\n) на концах
    if not line:
        continue # если строка пустая, пропускаем её
    if line.startswith('>'): # если строка начинается с >, это ID
        current_id = line[1:] # отрезаем первый символ > с помощью среза
        dna_dict[current_id] = "" # создаем пустое место для ДНК под этим ID
    else:
        # если это буквы, то просто прибавляем их к текущему ID
        dna_dict[current_id] = dna_dict[current_id] + line
best_id = "" # переменные для поиска максимума
max_gc = -1.0 # спец маленькое число, чтобы при сравнении первое число точно было больше
# считаем GC-состав для каждой ДНК в словаре
# 2 переменные - ключ и знач, items чтобы вытащить из словаря сразу ключ и знач, превращает словарь в список пар
for dna_id, dna_string in dna_dict.items():
    g_count = dna_string.count('G')
    c_count = dna_string.count('C')
    total_len = len(dna_string)
    gc_content = (g_count + c_count) / total_len * 100 # процент G и C в строке
    if gc_content > max_gc: # если нашли процент больше, чем был раньше — обновляем максимум
        max_gc = gc_content
        best_id = dna_id # присваиваем id
print(best_id)
print(round(max_gc, 6)) # oкругляем число до 6 знаков после запятой с помощью round()

#Double-Degree Array


