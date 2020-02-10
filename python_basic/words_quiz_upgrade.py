from random import randint

in_file = open("vocabulary.txt", "r")

kor = []
eng = []

for line in in_file:
    spl = line.strip().split(": ")
    kor.append(spl[1])
    eng.append(spl[0])

while True:
    ran_num = randint(1, len(kor)-1)
    eng_val = input("%s: " % kor[ran_num])

    if eng_val == "q":
        break

    if eng_val == eng[ran_num]:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % eng[ran_num])