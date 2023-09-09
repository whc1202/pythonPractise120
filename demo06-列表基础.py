# 列表也是序列对象，但它是容器类型，列表中可以包含各种数据
alist = [10, 20, 30, 'bob', 'alice', [1,2,3]]
# 计算列表长度
len(alist)
# 取出最后一项
lastOption = alist[-1]
print('最后一项是：' , lastOption)
# 因为最后一项是列表，列表还可以继续取下标
lastOptionLastWord = alist[-1][2]
print('列表最后一项的最后一个元素是：', lastOptionLastWord)

# 列表倒数第2项是字符串，再取出字符下标为2的字符,注意：不要正着取数，倒数取！
word = alist[-2][2]

print(word)
# ['bob', 'alice']
definedResult = alist[3:5:1]
print('特定结果为：',definedResult)
# 判断10在不在列表中
result1 = 10 in alist
# 判断o在不在列表中
result2 = 'o' in alist
# 判断100在不在列表中
result3 = 100 in alist
# 修改最后一项的值
alist[-1] = [1,2,3,4,5]
# 向aList列表中追加一项
# alist.append('hello,world!')