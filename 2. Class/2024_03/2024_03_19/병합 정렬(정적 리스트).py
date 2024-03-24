# 병합 정렬 함수 정의
def merge_sort(arr):
    # 만약 배열의 길이가 2 미만이면 배열을 그대로 반환
    if len(arr) < 2:
        return arr

    # 배열의 중간 인덱스를 찾음
    mid = len(arr) // 2
    # 배열을 중간 인덱스를 기준으로 두 개의 하위 배열로 나눔
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    # 병합된 배열을 저장할 리스트를 생성
    merged_arr = []
    l = h = 0
    # 두 하위 배열의 모든 요소를 병합할 때까지 반복
    while l < len(low_arr) and h < len(high_arr):
        # 두 하위 배열의 현재 요소를 비교하여 작은 값을 병합 배열에 추가
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    # 남은 요소를 병합 배열에 추가
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    # 병합된 배열을 반환
    return merged_arr



arr = [1,3,2,7,8,5,6,4,9,16,11,14,12,13,15,98,432,23,534,23,56,24,8,756]
print(merge_sort(arr))
