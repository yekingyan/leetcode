#!/usr/bin/python3
#用于反转正负数

def returnAbs(num):
    # 反转正值数
    a = str(num)
    b = len(a)
    s = 0
    for i in range(1, b + 1, 1):
        num1 = num % (10 ** i)
        num2 = int(num1 / (10 ** (i - 1)))
        ReNum = num2 * 10 ** (b - i)
        s += ReNum
    return s


def returnNum(num):
    if num > 0:
        ReNum = returnAbs(num)
        return ReNum
    else:
        # 如果为负数则先转为正值
        num = abs(num)
        returnAbs(num)
        ReNum = returnAbs(num)
        return -ReNum


def text_returnNum():
    nums = [
        (132456789, 987654231),
        (23456789, 98765432),
        (12345678, 87654321),
        (13160675555, 55557606131),
        (-132456789, -987654231),
        (-23456789, -98765432),
        (-12345678, -87654321),
        (-13160675555, -55557606131),
    ]
    for num in nums:
        original,expect = num
        exp = returnNum(original)
        e = "returnNum error,初始值：({}).计算值：({}).期待值：({})".format(original,exp,expect)
        assert exp == expect, e
        # print(returnNum(num))


if __name__ == '__main__':
    print(text_returnNum())
