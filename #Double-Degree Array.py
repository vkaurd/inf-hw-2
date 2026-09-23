#Double-Degree Array
file = open(r'c:\Users\user\Downloads\rosalind_ddeg.txt', 'r')
first_line = file.readline().split()
n = int(first_line[0])  # кол-во вершин
m = int(first_line[1])  # кол-во рёбер
degrees = [0] * (n + 1) # список из нулей для обычных степеней. n + 1, чтобы вершины имели номер индексов
# Создаем список списков для хранения соседей.
# Для каждой вершины от 0 до n изначально создаем пустой список []
neighbors = []
for i in range(n + 1):
    neighbors.append([])
for i in range(m): # читаем рёбра, считаем степени и заполняем списки соседей
    edge_line = file.readline().split()
    if not edge_line:
        continue
    u = int(edge_line[0])
    v = int(edge_line[1])
    # тк ребро соединяет обе вершины, +1
    degrees[u] = degrees[u] + 1
    degrees[v] = degrees[v] + 1
    neighbors[u].append(v)  # v — сосед для u
    neighbors[v].append(u)  # u — сосед для v
file.close()
# сумма степеней соседей для каждой вершины
double_degrees = [0] * (n + 1)
# Проходимся по каждой вершине от 1 до n
for vertex in range(1, n + 1):
    current_sum = 0
    # Перебираем всех соседей текущей вершины
    for neighbor in neighbors[vertex]:
        # Берем обычную степень соседа и прибавляем к сумме
        current_sum = current_sum + degrees[neighbor]
    double_degrees[vertex] = current_sum
for vertex in range(1, n + 1):
    print(double_degrees[vertex], end=" ")
print()
