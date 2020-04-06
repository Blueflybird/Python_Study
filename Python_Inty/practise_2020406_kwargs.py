def m1(*args,**kwargs):
    print('the type of args is', type(args))
    print('the type of kwargs is', type(kwargs))

# m1()
dic_inty={'name':'inty','age':'18 yeas old','height':'190cm'}

for k,v in dic_inty.items():
    print(k,':',v)
#--------------------------------------
#
# dic_inty={'name':'inty','age':'18 yeas old','height':'190cm','weight':'190lb'}
#
# def someone(dic_someone):
#     for k,v in dic_someone.items():
#         print(k,':',v)
# #someone(dic_inty)

#------------------**kwargs--------------------
def someone(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v)

someone(name='xiao hong', age='20', height='180')
