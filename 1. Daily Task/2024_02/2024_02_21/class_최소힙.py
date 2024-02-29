# 최소힙 : 부모가 자식보다 항상 작은 값을 유지하는 완전 이진 트리...
# 일차원 배열로서 작업...
# 삽입 : enqueue
# 삭제 : dequeue


# 삽입하는 연산 enqueue
# 완전 이진 트리를 유지하기 위해 추가되는 단말노드를 하나 삽입...!
# 단말노드를 기준으로 부모와 자리바꾸기를 진행...!
# (더 바꿀 필요가 없을 때까지..= "부모 < 자식", "부모x"
def enqueue(hq, item):
    # 단말노드를 item 을 추가하고...!
    hq.append(item)
    # 추가한 단말노드의 인덱스를 가져온다
    current = len(hq) - 1
    # 현재의 이 노드가 루트노드까지 진행했을 때까지 진행하면 종료...!
    while current != 1:
        # 부모의 인덱스값
        parent = current // 2
        # 부모의 요소보다 자식이 작은 경우...! (=자리바꾸기)
        if hq[parent] > hq[current]:
            hq[parent], hq[current] = hq[current], hq[parent]
            # 나 자신의 인덱스를 갱신...
            current = parent
        else:
            # 더 이상 자리바꾸기를 진행하지 않고 종료!
            break


# 삭제 : dequeue
# 힙의 삭제 과정은 루트 노드를 삭제하고, 가장 끝에 있는 단말노드를 루트노드로 가져온다...!
# 왼쪽 자식과 오른쪽 자식 중에서 나보다 더 작은 값이 있다면, 그 값과 자리바꾸기 진행...!
def dequeue(hq):
    data = hq[1]
    if len(heap) == 2: # 데이터가 하나만 있을 때
        return hq.pop()
    elif len(heap) == 1: # 비어있을 때
        return -1
    # 루트 노드 위치에 가장 끝에 있는 단말노드를 재배치
    hq[1] = hq.pop()
    current = 1
    N = len(heap)
    # 힙 자료구조가 유지되게끔 자리바꿈을 계속 진행...
    # 루트 노드부터 왼쪽 자식과 오른쪽 자식 중에서 나보다 더 작은값이 있다면 교체...!
    # 해당 값이 단말 노드까지 가게 되면 정지!
    while current < N:
        # 왼쪽/ 오른쪽 자식 인덱스
        left, right = current * 2, current * 2 + 1
        # 왼쪽과 오른쪽 자식이 모두 있는 경우
        if left < N and right < N:
            if hq[left] < hq[current] or hq[right] < hq[current]:
                # 자리교체를 수행해줘야 하는 경우이다...!
                # 왼쪽 자식과 오른쪽 자식 중에서 더 작은 것과 자리교체를 수행...!
                if hq[left] < hq[right]:
                    hq[left], hq[current] = hq[current], hq[left]
                    # 자리를 교체한 인덱스 또한 갱신
                    current = left
                else:
                    hq[right], hq[current] = hq[current], hq[right]
                    current = right
            else:
                break
        # 왼쪽 자식만 있는 경우
        elif left < N and right >= N:
            # 왼쪽 자식과 오른쪽 자식 중에서 더 작은 것과 자리교체를 수행...!
            if hq[left] < hq[current]:
                hq[left], hq[current] = hq[current], hq[left]
                # 자리를 교체한 인덱스 또한 갱신
                current = left
            else:
                break
        else:
            break
    return data


heap = [None]
enqueue(heap, 30)
enqueue(heap, 50)
enqueue(heap, 20)
enqueue(heap, 10)
enqueue(heap, 80)

for i in range(5):
    item = dequeue(heap)
    print(item)
