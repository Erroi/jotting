# encoding: utf-8
def func(message):
    def get_message(message):
        print('Got a message:{}'.format(message))
    return get_message(message)

func('hello')

def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message
    
send_message = func_closure()
send_message('hi')

def my_decorator1(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
    print('hello orange')

greet = my_decorator(greet)
greet()
# 变量greet指向了内部函数wrapper(),wrapper()中又调用了原函数greet(),
# my_decorator()就是一个装饰器，它把真正需要执行的函数greet()包裹在其中，并改变了他的行为，但是原函数不变。
@my_decorator1
def greet():
    print('hello orange')

greet()
# 可以把*args和**kwargs，作为装饰器内部函数wrapper()的参数，*args **kwargs,表示接受**任意数量和类型的参数**
def my_decorator2(func):
    @functools.wraps(func)  # 内置装饰器，保留原函数的元信息__name__等
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper


## 类装饰器
# 类装饰器依赖于函数__call__(),每当调用一个类的示例时，函数__call__()就会被执行一次
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print('hello world')

example()

# 装饰器嵌套
# 等效于 my_decorator1(my_decorator2(fun()))
@my_decorator1
@my_decorator2
def func():
    print('inner')





