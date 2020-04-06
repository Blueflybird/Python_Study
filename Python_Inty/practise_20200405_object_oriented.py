#object oriented
#------------------part1----------------------
# class Student():
#     def eat(self):
#         print("student can eat")
#     def study(self):
#         print("student can study")
#
# inty=Student()
# inty.study()

# Student().eat()

# friut="apple" #string本身就是一个面向对象
# print(friut.upper())
#------------------part2----------------------

# class Student:
#     def eat(self,name,age):
#         print(name+' can eat'+'and he is '+age)
#
# Student().eat('inty','18')

#------------------part3----------------------

# class Student:
#     def eat(self,name,age):
#         print(name,'can eat','and he is',age)
#
# Student().eat('inty','18')

class Student:
    name='inty'
    age=18

    def eat(self):
        print(self.name,'can eat','and he is',self.age) #注意加self
    @staticmethod #为了不用加self，但不能class里面的变量
    def walk():
        print('student can walk')
#Student().eat()
#Student().walk()

student1=Student() #创建
student1.eat()
student1.walk()

student2=Student()
student2.eat()
student2.walk()
