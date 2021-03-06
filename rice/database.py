# MySQL 属于典型的关系型数据库：
# 1. 数据库，是一些关联表的集合；而数据表则是数据的矩阵。
# 2. 在数据表中，每一列包含的是相同类型的数据；每一行则是一组相关的数据。
# 3. 主键也是数据表中的一个列，只不过，这一列的每行元素都是唯一的，且一个数据表中只能包含一个主键；
# 而外键则用于关联两个表。
# 4. 索引：对数据库表中一列或多列的值进行排序的一种结构。
#        优点：使用索引可以快速访问数据库表中的特定信息。可以对多列设置索引，检索指定列的时候就大大加快速度。
#        缺点：代价是插入数据变得更慢。