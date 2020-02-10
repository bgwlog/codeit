# 딕셔너리 타입: key값과 value값으로 구성
family = {}
family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'

# key 값 받기
print(family.keys())

# 특정 key 값 유무 판단
print('son' in family.keys())

# key값 리스트로 사용
key_list = list(family.keys())
print(key_list)

# 사전의 value값 받기
print(family.values())

# 특정 value 값 유무 판단
print('grace' in family.values())

# value값 리스트로 사용
value_list = list(family.values())
print(value_list)