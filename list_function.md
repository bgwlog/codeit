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
