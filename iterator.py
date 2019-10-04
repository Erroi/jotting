# encoding: utf-8
#  迭代器iterator
# 提供了一个next方法，调用这个方法后，要么得到这个容器的下一个对象，要么得到StopIteration的错误。
# 列表(list:[1,2,3]), 元组(tuple:(0,1,2,3))，字典(dict:{0:0,1:1,2:2}), 集合(set:set([0,1,2]))都是容器

# 可迭代对象
# 通过iter()函数返回一个迭代器，再通过next()函数实现遍历。

def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False
    
params = [
    1234,
    '1234',
    [1,2,3,4],
    set([1,2,3,4]),
    {1:1, 2:2, 3:3, 4:4},
    (1,2,3,4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))

# 除了Int类型，其他都是可以迭代的。


# 生成器
# 声明一个迭代器[i for i in range(1000)],每个生成的元素都会占用在内存中，占用大量的内存，于是生成器运用而生，
# 生成器：在调用next()的时候，才会生成下一个变量，(i for i in range(1000)),用小括号变初始化了一个生成器

# 验证数学的一个恒等式：(1 + 2 + 3 + ... + n) ** 2 = 1 ** 3 + 2 **3 + 3**3 + ... + n ** 3
def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1

gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

get_sum(8)