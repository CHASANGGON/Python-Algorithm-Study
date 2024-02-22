t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())

    binary_beat = [input() for _ in range(n)]
    decrypt_dict = {'0001101':0, '0011001':1, '0010011':2,
                    '0111101':3, '0100011':4, '0110001':5,
                    '0101111':6, '0111011':7, '0110111':8,
                    '0001011':9}
    
    # 암호의 시작점 범위 찾기 -> i & j
    for i in range(n):
        if '1' in binary_beat[i]:
            break
    for j in range(m-1,54,-1):
        if binary_beat[i][j] == '1':
            s = j - 55
            break

    # 암호 해독해서 완성하기
    decrypted = 0
    password = []
    for k in range(1,9):
        p = decrypt_dict[binary_beat[i][s:s+7]]
        s += 7
        if k % 2 == 0:
            decrypted += p
            password.append(p)
        else:
            decrypted += p*3
            password.append(p)
        

    # 판정
    if decrypted % 10:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum(password)}')