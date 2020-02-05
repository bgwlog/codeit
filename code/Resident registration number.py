def mask_security_number(security_number):
    # 코드를 입력하세요.
    num_list = list(security_number)
    for i in range(-4, 0):
        num_list[i] = "*"
    return ''.join(num_list)


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))