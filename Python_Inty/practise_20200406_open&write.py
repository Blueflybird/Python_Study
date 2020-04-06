#open('C:\GitHub\Pycharm Project\Python_Study\inty.txt')
# file=open('inty.txt') #同路径则不用写全路径
# text=file.read()
# print(text)
# file.close()

# with open ('inty.txt') as f:
#     print(f.read())

#---------------write----------
with open('inty.txt','a') as f: #a续写，w重写
    f.write('hello world\n')
