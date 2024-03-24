# 병합 병렬
def merge_sort(arr):
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left_arr, right_arr = arr[:mid], arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    k = 0
    l = r = 0

    # 정적 리스트와 다른점
    # pop.append를 사용하지 않고 원본 배열 arr에 값을 바로 바꿔준다
    # -> 위에서 left,right_arr 을 만들 때 슬라이싱을 통해서 만들었다.
    #   -> 그 결과 원본 리스트 arr과의 연결이 끊어졌기 때문에 아무 문제 없는 것이다..!
    while len(left_arr) > l and len(right_arr) > r:
        if left_arr[l] < right_arr[r]:
            arr[k] = left_arr[l]
            l += 1
        else:
            arr[k] = right_arr[r]
            r += 1
        k += 1


    if len(left_arr) > l:
        arr[k:] = left_arr[l:]


    if len(right_arr) > r:
        arr[k:] = right_arr[r:]



A = [9, 10, 6, 3, 2, 23, 1, 5, 7, 8]
# A = [6, 3, 2, 23]
merge_sort(A)
print(A)
