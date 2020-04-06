age=int(input("Please entre your age: "))

print(type(age))

if age<21:
    print("you can not smoke")

elif age==21:
    print("you are now 21, you can go to smoke")

elif age==100:
    print("you are 100 years old, please quit smoking")

else:
    print("you can smoke")
