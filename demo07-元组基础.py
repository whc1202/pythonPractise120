# 元组与列表基本上是一样的，只是元组不可变，列表可变。
atuple = (10, 20, 30, 'bob', 'alice', [1,2,3])
#求元组长度
len = len(atuple)
print(len)
#判断10在不在元组中
result1 = 10 in atuple
print(result1)
#取元组第二个元素
result2 = atuple[1]
print(result2)
#取元组从第三个元素开始 到第五个元素之前
result3 = atuple[2:4]
print(result3)
#尝试变元组的值，看是否能变化
# atuple[2] = 100000  此条不能执行，因为元组的元素是不能变化的