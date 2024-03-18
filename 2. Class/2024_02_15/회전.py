# 테스트케이스 수 T
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 수열의 길이 N, 회전 수 M
    N, M = map(int, input().split())
    # 수열의 요소들 arr
    arr = list(map(int, input().split()))

    # # 로직
    # 1. 선형큐 : arr 리스트를 사용해서 앞의 요소를 뒤로 한 개 이동...! (M번 반복)
    # for _ in range(M):
    #     x = arr.pop(0)  # dequeue, 시간복잡도 O(N)
    #     arr.append(x)  # enqueue,,,시간복잡도 O(1)
    # # 출력
    # print(f"#{tc} {arr[0]}")

    # # 2. 원형큐 : front, rear 변수...
    # # 0, 1, 2, 3, 4... -> n-1 -> 0 ... 인덱스가 순회...!
    # # 초기화
    # q = [0] + arr
    #
    # # 데이터가 꽉 차있는 상태....! (초기값으로 설정)
    # front = 0
    # rear = len(q) - 1
    # # M번 dequeue -> enqueue 반복 수행...
    # for _ in range(M):
    #     #     # dequeue 과정...
    #     #     front = (front + 1) % len(q)
    #     #     x = q[front]
    #     #     # enqueue 과정...
    #     #     rear = (rear + 1) % len(q)
    #     #     q[rear] = x
    
    # from collections import deque
    #
    # q = deque(arr)
    # # M번 dequeue -> enqueue 반복 수행...
    # # for _ in range(M):
    # #     # # dequeue 과정...
    # #     # x = q.popleft()
    # #     # # enqueue 과정...
    # #     # q.append(x)
    # #     q.rotate(1)
    # q.rotate(M)
    # print(q[0])

    # # 인덱스를 통해서 M번 순회하는 방법...
    # front = 0
    # for _ in range(M):
    #     front = (front + 1) % N
    # print(arr[front])
    # 인덱스가 +1 증가를 M번 순회하는 것이기 때문에...
    # 아래처럼 표현이 가능!
    print(arr[M % N])
    # # 출력
    # print(f"#{tc} {arr[0]}")