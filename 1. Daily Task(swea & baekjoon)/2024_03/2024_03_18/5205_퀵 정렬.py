def partition(left, right):
    left_copy = left
    pivot = arr[left]
    
    while left <= right:
        
        # pivot보다 큰 녀석 찾기 -> 후에 오른쪽으로 swap
        while left <= right and pivot >= arr[left]:
            left += 1
        
        # pivot보다 작은 녀석 찾기 -> 후에 왼쪽으로 swap
        while left <= right and pivot <= arr[right]:
            right -= 1
            
        # left와 right가 교차하지 않았다면, 둘의 위치가 올바르지 않다는 것
        # -> swap이 필요하다는 것
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[left_copy], arr[right] = arr[right], arr[left_copy]
    return right # pivot의 인덱스

def quick_sort(left, right):
    if left < right:
        pivot_idx = partition(left, right)
        
        quick_sort(left, pivot_idx-1)
        quick_sort(pivot_idx + 1, right)
        

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    quick_sort(0, n-1)
    print(f'#{tc} {arr[n//2]}')