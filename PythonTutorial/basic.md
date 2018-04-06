Basic
=====

# keyword

[keyword-list](https://www.programiz.com/python-programming/keyword-list)

```python3
In [1]: import keyword

In [2]: ', '.join(keyword.kwlist)
Out[2]: 'False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield'
```

# local variable

```python3
g = 0

# 在函数内容变量出现在等号前面就被视为局部变量,不论全局是否存在函数内使用的就是局部变量
def run1():
    print(g)
    g = 2
    print(g)

def run2():
    g += 2
    print(g)
```

## builtin variable

```python3
In [1]: import builtins

In [2]: ', '.join((i for i in dir(builtins) if i.islower() and '_' not in i))
Out[2]: 'abs, all, any, ascii, bin, bool, breakpoint, bytearray, bytes, callable, chr, classmethod, compile, complex, copyright, credits, delattr, dict, dir, display, divmod, enumerate, eval, exec, filter, float, format, frozenset, getattr, globals, hasattr, hash, help, hex, id, input, int, isinstance, issubclass, iter, len, license, list, locals, map, max, memoryview, min, next, object, oct, open, ord, pow, print, property, range, repr, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, tuple, type, vars, zip'
```

## sum

```python3
# sum(iterable[, start])

# [] + [1, 2] + [3, 4]
In [60]: sum([[1, 2], [3, 4]], [])
Out[60]: [1, 2, 3, 4]
```

##

```python3
# 先执行函数头后执行函数体
# [lambda, lambda, ...]
# [4x, 4x, ...]
In [62]: def create_multipliers():
    ...:     return [lambda x : i * x for i in range(5)]
    ...:

In [63]: for multiplier in create_multipliers():
    ...:     print(multiplier(2))
    ...:
8
8
8
8
8
```