"""
3. 列表排序
现在有2个列表：

In : A = [1, 3, 7, 10, 5, 2]

In : B = [2, 3, 5]
B 是 A 的子集，但顺序是乱的，编写一个函数用 A 中的元素顺序对 B 排序:

In  : my_sort(A, B)
Out: [3, 5, 2]
提示：使用列表自带的方法，enumerate
"""

from .two import unique


def my_sort(A, B):
    unique_A = unique(A)
    order_A = {num: index for index, num in enumerate(unique_A)}
    return sorted(B, key=lambda n: order_A[n])


if __name__ == '__main__':
    A = [1, 3, 7, 10, 5, 2]
    B = [2, 3, 5]

    result = my_sort(A, B)
    print(result)
