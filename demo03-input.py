# input用于获取键盘输入
inputContext = input('请输入一个数字：')
# input获得的数据是字符型
print(type(inputContext))
# 报错，不能把字符和数字做运算
# print(inputContext + 3)
# int可将字符串10转换成数字10
number = int(inputContext)
print(number, 'now the type is:', type(number))
# str将10转换为字符串后实现字符串拼接
print('现在可以进行字符串拼接了：' + str(number))
