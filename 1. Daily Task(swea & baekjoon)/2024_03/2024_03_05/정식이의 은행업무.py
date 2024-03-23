def find_origin():
    for twk in two_dict.keys():
        for thk in three_dict.keys():
            if two_dict[twk] == three_dict[thk]:
                print(f'#{tc} {two_dict[twk]}')
                return

def make_string(lst):
    string = ''
    for s in lst:
        string += s
    return string

t = int(input())

for tc in range(1,t+1):
    two = list(input())
    three = list(input())

    two_dict = {}
    for i in range(len(two)):
        if two[i] == '1':
            two[i] = '0'
            string = make_string(two)
            two_dict[string] = int(string, 2)
            two[i] = '1' # 복구
        else:
            two[i] = '1'
            string = make_string(two)
            two_dict[string] = int(string, 2)
            two[i] = '0' # 복구

    three_dict = {}
    for i in range(len(three)):
        if three[i] == '0':
            three[i] = '1'
            string = make_string(three)
            three_dict[string] = int(string, 3)
            three[i] = '2'
            string = make_string(three)
            three_dict[string] = int(string, 3)
            three[i] = '0' # 복구
        elif three[i] == '1':
            three[i] = '0'
            string = make_string(three)
            three_dict[string] = int(string, 3)
            three[i] = '2'
            string = make_string(three)
            three_dict[string] = int(string, 3)
            three[i] = '1' # 복구
        else:
            three[i] = '0'
            string = make_string(three)
            three_dict[string] = int(string, 3)
            three[i] = '1'
            string = make_string(three)
            three_dict[string] = int(string, 3)
            three[i] = '2' # 복구

    find_origin()