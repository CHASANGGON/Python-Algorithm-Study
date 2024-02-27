def run_f():
    for a in range(0,5):
        for b in range(1,6):
            for c in range(2,7):
                for d in range(3,8):
                    for e in range(4,9):
                        for f in range(5,10):
                            r = ''
                            r += str(a)
                            r += str(b)
                            r += str(c)
                            r += str(d)
                            r += str(e)
                            r += str(f)
                            run_lst.append(r)

def single_triplet():
    for a in range(10):
        t = ''
        t += str(a)
        t += str(a)
        t += str(a)
        t += str(a)
        t += str(a)
        t += str(a)
        triplet_lst.append(t)

def double_triplet():
    for a in range(10):
        for b in range(10):
            t = ''
            t += str(a)
            t += str(a)
            t += str(a)
            t += str(b)
            t += str(b)
            t += str(b)
            triplet_lst.append(t)



t = int(input())

for tc in range(1,t+1):

    card = list(input())
    card.sort()
    
    str_card = ''
    for c in card:
        str_card += c

    run_lst = []
    triplet_lst = []


    run_f()
    single_triplet()
    double_triplet()
    check_lst = run_lst + triplet_lst

    if str_card in check_lst:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')