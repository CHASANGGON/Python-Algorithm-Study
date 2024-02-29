def subset(i,k):
    if i == k:
        for j in range(N):
            if bit[j] == 1:
                print(arr[j],end='')
        print()
    else:
        for j in range(2):
            bit[i] = j
            subset(i+1,k)
            bit[i] = 0


N = 4
arr = [1,2,3,4]
bit = [0]*N
subset(0,N)