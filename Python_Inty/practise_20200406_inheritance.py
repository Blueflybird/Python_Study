class Father:
    def eat(self):
        print('Father can eat')

class Mother:
    def walk(self):
        print('walk like mother')

# class Son(Father):
#     pass #inheritance

#class Son(Father):
class Son(Father,Mother): #同时多个继承
    def eat(self):
        print('eat like son') #override

littleInty=Son()
littleInty.eat()
littleInty.walk()
