open_file = open("file_open.txt", "r")

for line in open_file:
    # print(line)
    # 빈줄 없애기
    print(line.strip())

open_file.close()
