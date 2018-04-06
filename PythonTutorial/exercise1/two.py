"""
2. 列表去重
要求：

编写一个函数，可以去除一个列表中重复的元素，并且保持元素的顺序：

In  : l = [1, 3, 6, 9, 3, 4, 1, 3]
In  : unique(l)
Out: [1, 3, 6, 9, 4]
提示：集合、Python3.6内置支持、列表解析（还没讲）、yield（还没讲）
"""


def unique(l):
    """
    Because index return the first index of a key, so use index to achieve deduplication.
    """
    cleaned_dict = {key: l.index(key) for key in l}
    reversed_cleaned_dict = {v: k for k, v in cleaned_dict.items()}
    result = [reversed_cleaned_dict[v] for v in sorted(reversed_cleaned_dict.keys())]
    return result


if __name__ == '__main__':
    l = [1, 3, 6, 9, 3, 4, 1, 3]
    res = unique(l)
    print(res)
