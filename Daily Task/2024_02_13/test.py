n = 5
values = [float(input()) for _ in range(n)]

num_dic = {}
for i in range(n):
    num_dic[chr(65+i)] = values[i]
    
print(num_dic)