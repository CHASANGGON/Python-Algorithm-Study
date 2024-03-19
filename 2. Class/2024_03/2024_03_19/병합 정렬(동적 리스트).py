# 병합 정렬
# 분할-정복 기법을 통해서 동작하는 정렬...!

def merge_sort(arr):
    # 기저조건(종료조건) : 배열의 요소가 2개 미만이라면 종료...!
    if len(arr) == 1:
        return
    
    # 1. Divide 나누는 단계 : arr 배열을 "절반씩" 나누어서 최소 배열이 될 때까지 반복한다.
    mid = len(arr) // 2
    
    # 왼쪽 배열, 오른쪽 배열... (슬라이싱)
    left_arr, right_arr = arr[:mid], arr[mid:]
    
    # 2. Conquer 정복 단계 : 정렬이 완수된 왼쪽 배열과, 오른쪽 배열을 각각 재귀적으로 진행한다...!
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    
    # 3. Combination 결합 단계 : 정렬된 왼쪽 배열과 오른쪽 배열을 병합하여 정렬된 새로운 리스트 배열을 만든다
    # 병합을 진행할 빈 리스트
    merge_arr = []
    # 왼쪽 배열과 오른쪽 배열의 각각 인덱스 변수 l, r
    l = r = 0
    
    # 왼쪽 배열의 요소가 비거나 또는 오른쪽 배열의 요소가 비거나 할 때까지 반복...
    while len(left_arr) > l or len(right_arr) > r:
        # 왼쪽 배열의 요소와 오른쪽 배열의 요소를 비교!
        if left_arr[l] < right_arr[r]:
            merge_arr.append(left_arr[l])
            l += 1
        else:
            merge_arr.append(right_arr[r])
            r += 1
            
            
    # 남은 요소를 병합 배열에 추가...!
    # while len(left_arr) > l:
    #     merge_arr.append(left_arr[l])
    #     l += 1
    # while len(right_arr) > l:
    #     merge_arr.append(right_arr[r])
    #     l += 1
    
    # 한 줄로 대체(슬라이싱)
    merge_arr += left_arr[l:] + right_arr[r:]
    
    return merge_arr
