out_file = open("vocabulary.txt", "w")

while True:
    eng = input("영어 단어를 입력하세요: ")
    if eng == 'q':
        break
    out_file.write(eng+": ")

    kor = input("한국어 뜻을 입력하세요: ")
    out_file.write(kor+"\n")

out_file.close()