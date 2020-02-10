class User:
    def say_hello(self):
        print("HELLO {}.".format(self.name))

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공")
        else:
            print("로그인 실패")


user1 = User()
user2 = User()

user1.name = "홍길동"
user1.email = "hong@abc.com"
user1.password = "12345"

user2.name = "김길동"
user2.email = "kim@abc.com"
user2.password = "12345"

User.say_hello(user1)
user1.say_hello()
# user1이 자동으로 파라미터로 넘어간다
