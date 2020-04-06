'''什么是*args'''
# def add(num1,num2,num3):
#     print(num1+num2+num3)
#
# add(1,1,2)

# def add(*args):
#     print(sum(args))
#
# add(1,1,2,2)

def add(*args):
    for name in args:
        print('i love',name)

add('我','是','天','才')
