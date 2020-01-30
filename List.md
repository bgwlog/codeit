리스트 함수
-------------------------------------

```python
numbers = [1, 2, 3, 4, 5]

#리스트 크기
len(numbers)

#리스트 값 추가(괄호 안에 추가할 값)
numbers.append(6) 

#리스트 값 추가2(괄호 안에 인덱스, 값)
numbers.insert(3, 9)

#리스트 값 삭제(대괄호 안에 제거할 인덱스)
del numbers[2]
del numbers[2:]

#리스트 정렬 두가지
sorted(numbers)
numbers.sort()
#둘의 차이는 sorted()는 정렬된 새 배열을 리턴해주고, .sort()은 해당 배열을 정렬시켜버림(+NONE 리턴)

```

리스트 꿀팁
---------------------------------------
# in / not in 키워드
## 어떤 값이 리스트에 있는지 확인
```python
# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))
# True / False

# 매번 위처럼 하기 귀찮다. in 이라는 키워드 사용하면 된다.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)
print(12 in primes)

# 값이 없는지 확인하려면 not in 키워드
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)
print(12 not in primes)

```

# 리스트 안의 리스트
```python
# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])

# 세 번째 학생의 성적
print(grades[2])

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0])

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1])

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)
```

# 추가 메서드
```python
#sort 메서드 (리스트를 정렬 상태로 바꿔줌)
numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)

#reverse 메서드 (리스트의 순서를 뒤집어줌)
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

#index 메서드 (괄호안의 값을 가지고 있는 원소의 인덱스를 리턴해줌)
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

#remove 메서드 (첫번째로 괄호안의 값을 가지고 있는 원소를 삭제)
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)
```
