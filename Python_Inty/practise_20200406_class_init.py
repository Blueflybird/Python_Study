# class Students:
#     name='inty'
#     age=18
#
#     def walk(self):
#         print(self.name,'can walk')
#         print(self.name,'is',self.age)
#
# s1=Students()
# s1.walk()
#
# s2=Students()
# s2.walk()

#-----------------init-----------------
class Students:
    def __init__(self,name,age):
        self.name=name #Students里面的name等于要初始化的name
        self.age=age #self指的就是Students

    def walk(self):
        print(self.name,'can walk')
        print(self.name,'is',self.age)

#s1=Students(name='inty',age='18')
s1=Students('inty','18')
#s1=Students('18','inty')
s1.walk()

s2=Students('James',15)
s2.walk()





