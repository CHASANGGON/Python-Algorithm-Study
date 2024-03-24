def merge(left, right):
    sorted_result = []
    while left and right: # 양쪽의 요소가 모두 하나 이상 존재할 때까지
        if left[0] > right[0]: # 오른쪽 값이 더 작으면
            sorted_result.append(right.pop(0)) # 오른쪽에서 pop한 요소를 push
        else: # 왼쪽 값이 더 작으면
            sorted_result.append(left.pop(0)) # 왼쪽에서 pop한 요소를 push

    if left: # 왼쪽의 요소가 남아 있다면
        sorted_result.extend(left)
    else:
        sorted_result.extend(right)
    
    return sorted_result # 정렬된 결과를 반환

def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr

    middle = length // 2
    left = merge_sort(arr[:middle]) # left  분할
    right = merge_sort(arr[middle:]) # right 분할
    
    return merge(left, right)
    

arr = [1,54,32,123,59,433,43,68,-1,5,6]
n = len(arr)

print(merge_sort(arr))
