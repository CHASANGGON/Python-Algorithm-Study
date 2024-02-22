n = int(input())

lst = [[0]*7 for _ in range(2)]

for j in range(4):
    lst[0][j] = n + j
for j in range(1,5):
    lst[1][-j] = n - j + 1

print(lst)