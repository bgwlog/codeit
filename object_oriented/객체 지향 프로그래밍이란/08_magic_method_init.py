# __init__ 메서드는 인스턴스가 생성될 때 자동으로 호출

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


# user1 = User()
# user1.initialize("Young", "young@codeit.kr", "123456")

# 위와 동일
user1 = User("Young", "young@codeit.kr", "123456")

print(user1.name, user1.email, user1.password)
