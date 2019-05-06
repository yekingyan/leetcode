#!/usr/bin/python3
# 用于反转正负数


# 方法一
def return_abs(num):
    # 反转正值数
    a = str(num)
    b = len(a)
    s = 0
    for i in range(1, b + 1, 1):
        num1 = num % (10 ** i)
        num2 = int(num1 / (10 ** (i - 1)))
        re_num = num2 * 10 ** (b - i)
        s += re_num
    return s


def return_num(num):
    if num > 0:
        re_num = return_abs(num)
        return re_num
    else:
        # 如果为负数则先转为正值
        num = abs(num)
        return_abs(num)
        re_num = return_abs(num)
        return -re_num


# 方法二
def reverse(x):
    if x < 0:
        x = abs(x)
        x = ''.join(reversed(str(x)))
        re_num = int('-' + x)
    else:
        x = ''.join(reversed(str(x)))
        re_num = int(x)
    if re_num < -2**31 or re_num > 2**31:
        return 0
    else:
        return re_num


# 方法三
def reverse3(x):
    if x < 0:
        x = abs(x)
        x = str(x)[::-1]
        re_num = int('-' + x)
    else:
        x = str(x)[::-1]
        re_num = int(x)
    if re_num < -2**31 or re_num > 2**31:
        return 0
    else:
        return re_num

def reverse4(num: int) -> int:
  str_n = str(num)
  reverse_str = ''.join(reversed(str_n))
  if '-' in reverse_str:
    reverse_n = int('-' + reverse_str[:-1])
    return reverse_n if reverse_n > -2**31 else 0
  else:
    reverse_n = int(reverse_str)
    return reverse_n if reverse_n < 2**31-1 else 0


def test():
    nums = [
        (132456789, 987654231),
        (23456789, 98765432),
        (12345678, 87654321),
        (1675555, 5555761),
        (-132456789, -987654231),
        (-23456789, -98765432),
        (-12345678, -87654321),
        (-1375555, -5555731),
        (-2**32, 0),
        (2**31, 0),
    ]
    for num in nums:
        original, expect = num
        # exp = return_num(original)
        exp = reverse4(original)
        # exp = reverse3(original)
        e = "returnNum error,初始值：({}).计算值：({}).期待值：({})".format(original, exp, expect)
        assert exp == expect, e
        # print(returnNum(num))


if __name__ == '__main__':
    print(test())
