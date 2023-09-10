a = 10
b = 20

if a < b:
    smaller = a
else:
    smaller = b

print(smaller)

# 写一个和上面的if-else语句等价的三目运算符语句
# resultA if condition else resultB
s = a if a<b else b

print(s)