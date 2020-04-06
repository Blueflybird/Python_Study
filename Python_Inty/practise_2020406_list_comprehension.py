'''
list comprehension
list 生成新list的过程就是list comprehension的一种

我的需求：
从0-10的数字分别乘以2，
然后放到新的列表（list）里
'''
# #--------------part 1------------------
# newList=[]
# print(newList)
#
# for i in range(11):
#     newList.append(i*2)
# print(newList)
#
# #--------------Syntactic sugar----------
# print([i*2 for i in range(11)])

#--------------part 2------------------
list=['小明','网吧','小红','小丽']
emptyList=[]
for name in list:
    if name.startswith('网'):
        #print(name)
        emptyList.append(name)
print(emptyList)

print([name for name in list if name.startswith('小')])

