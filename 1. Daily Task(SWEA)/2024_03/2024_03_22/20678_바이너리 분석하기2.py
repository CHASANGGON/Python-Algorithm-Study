t = int(input())

b_to_h = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
       10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', }

h_to_b = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', 
          '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001',  
          'A':'1010','B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

for tc in range(1,t+1):
    length, bits = input().split()
    length = int(length)
    if length == 24:
        num = ''
        for i in range(6):
            num += b_to_h[int(bits[i*4:i*4+4], 2)]
        while num[0] == '0':
            num = num[1:]
    else:
        num = ''
        for b in bits:
            num += h_to_b[b]
    
    print(f'#{tc} {num}')