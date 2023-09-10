# 想用switch-case来写,但是发现python不支持switch语法

score = int(input("请输入你的分数："))
if score<60:
    print('不及格，你该努力了！')
elif(60 <= score < 70):
    print('及格了，但是还是要努力！')
elif(70<=score<80):
    print('下次争取良好！')
elif(80<=score<90):
    print('良好了，下次争取优秀！')
elif(90<=score<100):
    print('优秀了，下次要争取拿满分')
elif(score==100):
    print('已经满分了，太厉害了！')
else:
    print('你输入的成绩过于离谱！')
