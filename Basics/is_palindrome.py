def is_palindrome(x):
    a = str(x)
    return a[::-1] == a
    # s = str(x)
    # i, j = 0, len(s)-1
    # while i < len(s):
    #     if s[i] != s[j]:
    #         return False
    #     i += 1
    #     j -= 1
    # return True


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')