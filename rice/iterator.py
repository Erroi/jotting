# this python file uses the following encoding: utf-8
from functools import reduce;
def fn(x,y):
    return x * 10 + y

a = reduce(fn, [1,3,5,7,9])
print(a)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

b = reduce(fn, map(char2num, '13579'))
print(b)

def square(s):
    return int(s) * 2

c = map(square, '324335342423')
print(c)

## 埃氏筛选：求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始化序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome('12321'), is_palindrome('909a'))


# sorted
sorted([34,52,3,23,-53,-9,2])
sorted([34,52,3,23,-53,-9,2], key=abs)
sorted(['bob', 'Zoo', 'Credit', 'stuff'])
sorted(['bob', 'Zoo', 'Credit', 'stuff'], key=str.lower)
sorted(['bob', 'Zoo', 'Credit', 'stuff'], key=str.lower, reverse=True)



