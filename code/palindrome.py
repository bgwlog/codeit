def is_palindrome(word):
    # 코드를 입력하세요.
    torf = True

    for i in range(int(len(word)/2)):
        if word[i] != word[len(word) - i - 1]:
            torf = False
            break
        else:
            continue

    return torf


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
