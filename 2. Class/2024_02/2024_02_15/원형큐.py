# 선형큐와 다른 점은 rear 와 front에 % SIZE를 하는 것
SIZE = 10
queue = [0] * SIZE

front = rear = 0  # 초기화


# 큐 삽입 연산 enqueue
def enqueue(item):
    global rear
    # 큐가 이미 꽉 찬 상태일 때에는 삽입 불가...!
    if is_full():
        return -1
    # 꼬리 rear를 1 증가 시키고 그 위치에 요소를 삽입...!
    rear = (rear + 1) % SIZE
    queue[rear] = item


# 큐 삭제 연산 dequeue
def dequeue():
    global front
    if is_empty():
        return -1
    # 머리 front 1 증가 시키고 그 위치의 요소를 반환...
    front = (front + 1) % SIZE
    return queue[front]


# 보조 연산...
# is_full : 가득 차 있는 상태...
def is_full():
    # 머리와 꼬리가 맞닿은 상태..!
    return (rear + 1) % SIZE == front


# is_empty : 비어있는 상태...
def is_empty():
    return front == rear


# q_peek : 꺼낼 요소를 미리 확인해볼 수 있는 peek.
def q_peek():
    return queue[(front + 1) % SIZE]


# 큐를 구현하여서 1, 2, 3 원소를 순서대로 삽입
# 큐에서 값을 3개를 꺼내 차례대로 출력한다...!
enqueue(1)
enqueue(2)
enqueue(3)

item = dequeue()
print(item)
item = dequeue()
print(item)
item = dequeue()
print(item)