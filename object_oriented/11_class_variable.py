# 클래스변수: 한 클래스의 모든 인스턴스가 공유하는 속성
# - 클래스변수 값 읽는 법
#   1. 클래스 이름.클래스 변수 이름
#   2. 인스턴스 이름.클래스 변수 이름
# - 클래스 변수 값 설정
#   1. 클래스 이름.클래스 변수 이름

class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1
#       그냥 count += 1 은 에러나네~


user1 = User("k1", "k1@abc.com", "12345")
user2 = User("k2", "k2@abc.com", "12345")
user3 = User("k3", "k3@abc.com", "12345")

# 클래스 변수
print(User.count)

# 인스턴스 변수
user1.count = 50
print(user1.count)

# 같은 이름의 클래스 변수 VS 같은 이름의 인스턴스 변수
# User.count          vs  user1.count
# 인스턴스 변수가 읽어짐.
# -> 클래스 변수에 값을 설정할 때는 클래스 이름으로만!