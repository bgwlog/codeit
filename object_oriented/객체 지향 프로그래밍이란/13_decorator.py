def say_hello():
    print("Hello")

def add_to_something(func):
    def wrapper():
        print("START")
        func()
        print("END")

    return wrapper

# 출력하는 방법
add_to_something(say_hello)()
# 또는
print("===========================")
new_say_hello = add_to_something(say_hello)
new_say_hello()