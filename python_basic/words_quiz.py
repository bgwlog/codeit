in_file = open("vocabulary.txt", "r")

kor = []
eng = []

for line in in_file:
    result = line.split(":")
    eng.append(result[0].strip())
    kor.append(result[1].strip())

for i in range(len(kor)):
    print("%s: " % kor[i])
    answer = input()

    if answer == eng[i]:
        print("맞았습니다.")
    else:
        print("아쉽습니다. 정답은 %s입니다." % eng[i])