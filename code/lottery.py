from random import randint


# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    # 코드를 입력하세요
    random_list = []
    while len(random_list) < 7:
        ran = randint(1, 45)
        if ran not in random_list:
            random_list.append(ran)
        random_list.sort()

    return random_list


# 보너스까지 포함해 7개 숫자 뽑기s
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    # 코드를 입력하세요
    lotto_list = generate_numbers()
    while len(lotto_list) < 7:
        ran = randint(1, 45)
        if ran not in lotto_list:
            lotto_list.append(ran)

    return lotto_list


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # 코드를 입력하세요
    count = 0
    if len(list1) > len(list2):
        input_lotto = list2
        answer_lotto = list1
    else:
        input_lotto = list1
        answer_lotto = list2
    for val in input_lotto:
        if val in answer_lotto:
            count += 1
    return count


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 코드를 입력하세요
    new_list = []
    for i in range(len(numbers)):
        new_list.append(winning_numbers[i])
    bonus_number = winning_numbers[6]
    bonus_list = [bonus_number]

    fir_count = count_matching_numbers(numbers, new_list)
    sec_count = count_matching_numbers(numbers, bonus_list)

    # 위의 보너스 숫자 리스트를 뽑아내서 보너트카운트를 얻는 방법 업그레이드
    # bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if sec_count == 1:
        if fir_count == 5:
            return 50000000
        return 0
    else:
        if fir_count == 3:
            return 5000
        elif fir_count == 4:
            return 50000
        elif fir_count == 5:
            return 1000000
        elif fir_count == 6:
            return 1000000000
        else:
            return 0
        return 0