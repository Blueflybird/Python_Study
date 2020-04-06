"""
Python3 中有六个标准的数据类型

Nummer（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
"""
myList=(1,2,3,4)
myDictionary={"key":"value","key2":"value"}
print(myDictionary)

myPhones={"Iphone X":1000,"Sumsang S9":900}
print(myPhones)

#access dic keys
Iphone_Price=myPhones["Iphone X"]
print("Iphone price: "+str(Iphone_Price))

#change key values
myPhones["Iphone X"]=500
print(myPhones)

myPhones.clear()
print(myPhones)
