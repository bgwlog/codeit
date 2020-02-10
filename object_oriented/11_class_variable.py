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

print(User.count)
