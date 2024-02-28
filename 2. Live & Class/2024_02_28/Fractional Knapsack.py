# 물건을 원하는 만큼 자를 수 있는 knapsack 문제
n = 3 # 물건 3개
target = 30 # kanpsack 30 kg
thins = [(5, 50), (10, 60), (20, 140)] # (kg, price)
# kg당 가격으로 내림차순 정렬
thins.sort(key = lambda x : (x[1] / x[0] ), reverse = True)

sum = 0 

for kg, price in thins:
    per_price = price / kg
    # 만약 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝난다.
    if target < kg:
        sum += target * per_price
        break

    sum += price
    target -= kg
print(int(sum))