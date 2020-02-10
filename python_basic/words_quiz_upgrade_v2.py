from random import randint

in_file = open("vocabulary.txt", "r")

voca_dic = {}

for line in in_file:
    data = line.strip().split(": ")
    eng_word = data[0]
    kor_word = data[1]

    voca_dic[eng_word] = kor_word

while True:
    keys = list(voca_dic.keys())

    index = randint(1, len(keys) - 1)

    input_val = input("%s: " % voca_dic[keys[index]])

    if input_val == "q":
        break

    if input_val == keys[index]:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 %s입니다." % keys[index])