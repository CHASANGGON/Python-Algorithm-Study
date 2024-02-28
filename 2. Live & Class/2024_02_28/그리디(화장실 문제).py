# a 15 / b 30 / c 50 / d 10

person = [15,30,50,10]
n = len(person)
person.sort()
sum = 0
left_person = n - 1

for turn in range(n):
    time = person[turn]

    sum += left_person * time
    left_person -= 1

print(sum)