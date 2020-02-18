# 또 다른 데코레이터 사용방법
def add_to_something(func):
    def wrapper():
        print("START")
        func()
        print("END")

    return wrapper

@add_to_something
def say_hello():
    print("Hello")


# 출력하는 방법
say_hello()