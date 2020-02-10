from random import randint

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

a = randint(0, 9)
while True:
    b = randint(0, 9)
    if a != b:
        break
while True:
    c = randint(0, 9)
    if c != b and c != a:
        break
# 리스트에 값 저장
ran = [a, b, c]

count = 0

while True:
    strike = 0
    ball = 0

    print("세 수를 하나씩 차례대로 입력하세요.")

    while True:
        i = int(input("1번째 수를 입력하세요: "))
        if 0 <= i < 10:
            break
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")

    while True:
        j = int(input("2번째 수를 입력하세요: "))
        if j == i:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        else:
            if 0 <= j < 10:
                break
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")

    while True:
        k = int(input("3번째 수를 입력하세요: "))
        if k == i or k == j:
            print("중복되는 수 입니다. 다시 입력해주세요.")
        else:
            if 0 <= k < 10:
                break
            print("범위를 벗어나는 수입니다. 다시 입력해주세요.")

    # 리스트에 입력값 저장
    inp = [i, j, k]
    index = 0

    # 랜덤 리스트에 값이 있는지 (s b 카운팅)
    while True:
        if inp[index] in ran:
            if inp[index] == ran[index]:
                strike += 1
            else:
                ball += 1
        index += 1
        if index == 3:
            break

    print("%dS %dB" % (strike, ball))
    count += 1

    if strike == 3:
        break

print("축하합니다. %d번만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)
