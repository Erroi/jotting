# This Python file uses the following encoding: utf-8
# list 和 tuple 都是一个可以放置任意数据的有序集合
# list 是动态的，长度大小不固定，可以增删；tuple是静态的，长度大小固定，不可增删。
l = [1,2,3,4]
l[3] = 40
l
[1,2,3,40]
l.append(5)
l.remove(3)
l[-1]
l[1:3]
[2,3]


tup = (1,2,3,4)
# tup[3] = 40
# typeError
new_tup = tup + (5, )
new_tup
(1,2,3,4,5)
tup[-1]
tup[1:3]
(2,3)

# 互相转换
list((1,2,3))
[1,2,3]

tuple([1,2,3])
(1,2,3)

# 内置函数
l = [3,2,3,7,8,1]
l.count(3)
2
l.index(7)
3
l.reverse() # 修改了原list
l
[1,2,7,3,2,3]
l.sort() # 修改原list
l
[1,2,3,3,7,8]
list(reversed(l))
sorted(l) # 不改变原list，返回新的list

tup = (3,2,3,7,8,1)
tup.count(3)
2
tup.index(7)
3
list(reversed(tup)) # reversed object需要list转下
[1,8,7,3,2,3]
sorted(tup) # sorted 同时转换为list
[1,2,3,3,7,8]

# list tuple存储方式差异: list 要比 tuple多16字节，因为list是动态的，需要存储指针指向对应的元素（8字节）；
# 另外需要额外存储已经分配的长度大小（8字节），以便及时分配额外空间
l = [1,2,3]
l.__sizeof__()
64

tup = (1,2,3)
l.__sizeof__()
48 # tuple 长度大小固定，元素不可变，所以存储空间固定

l = [] # sizeof 40
l.append(1) # sizeof 72: 72-40 / 8 = 4,分配了4个元素空间
l.append(2) # size0f 72
l.append(3) # sizeof 72
l.append(4) # sizeof 72
l.append(5) # sizeof 104 加入第五个元素后，列表空间不足，所以又分配了4个元素


# dict: 字典： 一系列由key和value配对组成的元素集合，有序
# set：集合：一系列无序的、唯一的元素组合
# dict和set的内部数据结构都是一张哈希表，对于dict，存贮了哈希值hash、键、值；对于集合，存贮了哈希值和单一元素。
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
d1 == d2 == d3 == d4
True
d1['name']
d1.get('name', 'null')
'name' in d1
True
'location' in d1
False
d1['school'] = 'university'
d1['dob'] = '93-11'
d1['name'] = 'Inky'
d1.pop('dob')

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键升序排
[('a', 2),('b', 1),('c', 10)]
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值升序排
[('b', 1),('a', 2),('c', 10)]

s1 = {1,2,3,'hello'}
s2 = set([1,2,3,'hello'])
s1 == s2
True
# set 本质上是一个哈希表，不支持索引
1 in s1
True
10 in s1
False
s1.add(4)
s1.remove(4)
s3 = {3,4,2,5}
sorted(s3) # 对集合的元素进行升序排列
[2,3,4,5]


# 字符串 不可变的immutable
s = 'a\nb\tc'    # n 换行符，t为制表符
len(s) # 5
name = 'jasson'
name[0]
'j'
name[1:3]
'as'
for char in name:
  print(char)
'j' 'a' 's' 's' 'o' 'n'

# s[0] = 'H' typeError
s.replace('h', 'H')
str1 = 'jssf'
str2 = 'a'
str1 += str2 # 会先检查str1有没有其他的引用。如果没有的话，就会尝试原地扩充字符串buffer的大小，而不是重新分配内存来创建新的字符串并copy
l = ['s', 'sf', 'e']
s1 = '-'.join(l)
path = 'hive://dob/training'
path.split('//')[1].split('/')[0] # dob
s2 = ' my name is jasson '
s2.strip()
s2.lstrip()
s2.find('s', 3, 8) # 7
s2.find('g') # -1
num = 23123
name = 'jason'
'this is id: {}, name: {}'.format(num, name) # string.format() 格式化，{} 预留的格式符，为变量id name预留位置
'this is id: %d, name: %s' % (num, name) # 也是格式化 %d:整型，%s:字符串

name = input('your name:')
gender = input('you are a boy?(y/n)')

int('4') # string 强制转换为 int
int('3.2') # ValueError
float('4') # 转为 float 4.0
float('4.98') # 4.98


import json
params_string = json.dumps({'symbol': '123456'}) # 将基本数据类型序列化为string
json.loads(params_string) # 将一个合法字符串反序列化为python的基本数据类型
# 但也请注意，一定要catch


# 遍历
d = {'name': 'jason', 'dob': '93', 'gender': 'male'}
for k in d:   # 遍历键
  print(k)
'name'
'dob'
'gender'

for v in d.values():    # 遍历字典的值
  print(v)

for k,v in d.items():   # 遍历key：value
  print('key:{}, value: {}'.format(k, v))


l = [1,3,2,34,23,7]
for index in range(0, len(l)):
  if index < 5:
    print(l[index])

range(0, len(l)) # 拿到l的索引0，1，2，3

for index, item in enumerate(l):
  if index < 8:
    print(item)

enumerate(l) # 可分别遍历到index和item

for index, item in enumerate(l):
  if index > 8:
    continue  # continue: 如果index > 8的话，跳出这层循环，直接进入下次循环
  print(item)

while True:
  try:
    text = input('Please enter you questions, enter q to exit')
    if text == 'q':
      print('Exit system')
      break
    print(text)
  except ValueError as err:
    print('Encountered error:{}'.format(err))
    break
  # 捕获所有类型的错误
  except Exception as err:
    print('Exception')
  finally:
    print('最终都会执行')

try: 
  # 自定义错误
  raise NameError('hello')
except NameError:
  print('custom error')
# 错误类型：ZeroDivisionError NameError TypeError KeyError FileNotFountError IndexError JSONDecodeError
# Exception 是其他所以非系统异常的基类，能够匹配任意非系统异常

# 条件与循环一并 expression1 if condition else expression2 for item in iterable
# expression for item in iterable if condition
# y = 2 * |x| + 5
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in l]

text = ' Today, is , Sunday'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 5]
print(text_list) # ['Today', 'Sunday']

x = (3,2,54)
y = (435,21,9)
tup3 = [(xx,yy) for xx in x for yy in y if xx != yy]
# 等价于
l = []
for xx in x:
  for yy in y:
    if xx != yy:
      l.append((xx, yy))

# [{key: val[index] for index,key in enumerate(attributes)} for val in values ]


# module

# utils/utils.py
def get_sum(a, b):
  return a + b

if __name__ == '__main__':    # 在import导入的时候，会自动把所有报漏在外的执行一遍，可以放到这个下面
  print('testing')            # 原因：__name__作为Python的魔术内置参数，本质上是模块对象的一个属性，当使用import时，
                              #      __name__就会被赋值为该模块的名字，自然就不等于__main__了。

# utils/class_utils.py
class Encoder(object):
  def encode(self, s):
    return s[::-1]

class Decoder(object):
  def decode(self, s):
    return ''.join(reversed(list(s)))

# src/sub_main.py
import sys
sys.path.append('..')       # 表示当前目录程序所在位置向上提了一级，便可以掉utils的模块了
# from utils.utils import *   # 调用子目录的模块是，只需要使用.代替/来表示子目录
encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))



