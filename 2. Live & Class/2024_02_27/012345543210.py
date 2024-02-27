def f(x, y):
    if x == y:
        return
    print(x,end=' ')
    f(x+1, y)
    print(x,end=' ')

f(0,6)