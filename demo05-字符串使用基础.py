# python中，单双引号没有区别，表示一样的含义
sentence = 'tom\'s pet is a cat'  # 单引号中间还有单引号，可以转义
sentence2 = 'tom said :\"hello,world!\"'
print(sentence2)

py_str = 'python'

# 取长度
length = len(py_str)

# 第一个字符
firstChar = py_str[0]

# 最后一个字符
lastChar = py_str[-1]

# py_str[6]  # 错误，下标超出范围

# 切片 注意：起始下标包含，结束下表不包含
partChar = py_str[2:4]
print(partChar)

# 从2开始取，取到结束
partChar1 = py_str[2:]

# 从头开始取，取到5之前
partChar2 = py_str[:5]
print("从2开始取的输出结果：" + partChar1)
print("取到5之前的输出结果：" + partChar2)

# 全部取出
fullChar = py_str[:]
print("全部取出的输出结果：" + fullChar)

# 设置步长。在这里步长为2
partChar3 = py_str[::2]
print("步长为2的输出结果：" + partChar3)

# 从第二个字符开始取 步长为2
partChar4 = py_str[1::2]
print("从第二个字符开始取 步长为2的输出结果：" + partChar4)

# 倒叙取出
convertChar = py_str[::-1]
print("倒序将所有元素取出：" + convertChar)

# 将所有字符重复打印3次
repeatChar = py_str * 3
print("字符串打印3次的结果是：", repeatChar)
