import functools # functools.wraps，它的作用是协助构建行为良好的装饰器。

def clock(func):
    """装饰器，计算被装饰函数的运行时间"""
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f"{k}={v}" for k, v in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print(f"{elapsed:0.8f} {name}({arg_str}) -> {result}")
        return result
    return clocked

# 分派函数
# 使用@singledispatch装饰的普通函数会变成泛函数（generic function）：根据第一个参数的类型，以不同方式执行相同操作的一组函数。
# singledispatch机制的一个显著特征是，你可以在系统的任何地方和任何模块中注册专门函数。如果后来在新的模块中定义了新的类型，可以轻松地添加一个新的专门函数来处理那个类型。此外，你还可以为不是自己编写的或者不能修改的类添加自定义函数。
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return "<pre>{}</pre>".format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return "<p>{0}</p>".format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x})</pre>".format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)  # 可变序列
def _(seq):
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ur>\n<li>" + inner + '</li>\n</ul>'


# 装饰器工厂函数：带参数的装饰器
# 装饰器工厂函数必须作为函数调用，并且传入所需的参数。
# 即使不传入参数，register也必须作为函数调用
registry = set()
def register(active=True):
    def decorate(func):
        print("running register(active{}) -> decorate({})".format(active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate