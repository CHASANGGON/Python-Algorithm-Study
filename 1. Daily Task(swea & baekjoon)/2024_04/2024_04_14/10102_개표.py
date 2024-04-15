n = int(input())
lst = input()
a = lst.count('A')
b = lst.count('B')
if a == b:
    print('Tie')
elif a > b:
    print('A')
else:
    print('B')