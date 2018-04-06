"""
4. FIZZBUZZ
遍历并打印1到20，如果数字能被3整除，显示Fizz；如果数字能被5整除，显示Buzz；如果能同时被3和5整除，就显示FizzBuzz：

❯ python 4.py
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
"""


def fizzbuzz(n):
    if (not n % 3) and (not n % 5):
        return 'FizzBuzz'
    elif not n % 3:
        return 'Fizz'
    elif not n % 5:
        return 'Buzz'
    else:
        return n


if __name__ == '__main__':
    for i in range(1, 21):
        print(fizzbuzz(i), end=' ')
    print()
