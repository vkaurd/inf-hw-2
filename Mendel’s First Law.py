#Mendel’s First Law
file = open(r'c:\Users\user\Downloads\rosalind_iprb.txt', 'r')
line = file.readline()
file.close()
parts = line.split() # разрезаем строчку по пробелам
# переводим строчки в генетические переменные
AA = int(parts[0])
Aa = int(parts[1])
aa = int(parts[2])
total = AA + Aa + aa # общее количество особей
prob_aa_aa = (aa / total) * ((aa - 1) / (total - 1)) * 1.0 # aa-1 тк одну пару уже почитали, ее нет в списке
# *2, тк порядок родителей может быть разным. Шанс aa — 50% (0.5)
prob_Aa_aa = (Aa / total) * (aa / (total - 1)) * 0.5 * 2
# шанс aa равен 25% (0.25)
prob_Aa_Aa = (Aa / total) * ((Aa - 1) / (total - 1)) * 0.25
total_bad_prob = prob_aa_aa + prob_Aa_aa + prob_Aa_Aa # cуммируем вероятность a
result = 1 - total_bad_prob # хотя бы один A
print(round(result, 5)) # ответ, округленный до 5 знаков