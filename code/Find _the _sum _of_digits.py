# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    sum = 0
    tostr = str(num)
    for i in range(len(tostr)):
        sum += int(tostr[i])
    return sum
# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
sum = 0

for i in range(1, 1001):
    sum += sum_digit(i)

print(sum)