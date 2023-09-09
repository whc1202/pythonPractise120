# 字典是key-value(键－值）对形式的，没有顺序，通过键取出值
adict = {'name': 'bob', 'age': 23}
len(adict)
# 注意：字典是通过key取值的！！！
'bob' in adict  # False
'name' in adict  # True
adict['email'] = 'bob@tedu.cn'  # 字典中没有key，则添加新项目
adict['age'] = 25  # 字典中已有key，修改对应的value
