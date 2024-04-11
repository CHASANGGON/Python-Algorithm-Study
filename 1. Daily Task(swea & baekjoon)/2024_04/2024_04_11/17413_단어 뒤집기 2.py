import sys
input = sys.stdin.readline

string = input().rstrip()
length = len(string)
idx = 0
while idx < length:
    # 태그
    if string[idx] == '<':
        tag = ''
        while string[idx] != '>':
            tag += string[idx]
            idx += 1
        tag += '>'
        idx += 1
        print(tag,end='')
    
    # 일반 문자
    else:
        if string[idx] == ' ':
            idx += 1
            print(' ',end='')
        word = ''
        while idx < length and (string[idx] != ' ' and string[idx] != '<'):
            word += string[idx]
            idx += 1
        print(word[::-1],end='')
