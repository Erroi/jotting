# encode = 'utf-8'
int('34')
str(45)
bool('sfdf')

type('34')

# 重复操作 * 7
print('hello' * 3) # hellohellohello

zadiac_days = ((1,20), (2,19), (3, 21), (4,21), (5, 21), (6,21))
(month, day) = (2, 15)
zadiac_day = filter(lambda x: x <= (month,day), zadiac_days)
print(list(zadiac_day))

list1 = [2,3,4,5]
l1 = [i*i for i in list1 if(i % 2) == 0]
print(l1)

dict1 = {i:0 for i in list1 if(i % 2) == 0}
print(dict1)

file1 = open('name.txt', 'w')
file1.write('诸葛亮\r')
file1.write('周瑜')
file1.close()

file2 = open('name.txt')
# print(file2.read())
print(file2.tell()) # 当前读取文件的指针
print(file2.readline())
file2.seek(0)
print(file2.tell())
# for text in file2.readlines():
#     print('---', text)
file2.close()

def readNum(first, *other):
    print(1 + len(other))

readNum(3,5,9)

# 迭代器 iter()
list2 = [33,2,45,9]
it = iter(list2)
print(next(it))
print(next(it))
