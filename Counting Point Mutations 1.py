#Counting Point Mutations 1
file = open('c:/Users/user/Downloads/rosalind_hamm.txt', 'r')
lines = file.readlines()
file.close()
s = lines[0].strip() # достаем первую и вторую строки, очищая их от переноса строк(невидимых символов) (\n) - strip()
t = lines[1].strip()
hamming_distance = 0 # счетчик для несовпадений
for i in range(len(s)): # тк строки s и t одинаковой длины, используем len(s)
    if s[i] != t[i]: # сравниваем символы на одной и той же позиции i
        hamming_distance = hamming_distance + 1
print(hamming_distance)