"""
5. 编写过滤1-100中的素数的函数
提示：使用filter
"""

from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)+1)):
            if not n % i:
                return False
        return True


def get_prime(max):
    for i in filter(is_prime, range(1, max+1)):
        yield i


if __name__ == '__main__':
    for i in get_prime(100):
        print(i)
