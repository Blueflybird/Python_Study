def converter(weight):
    ponds=weight/0.45
    print(ponds)

converter(60)
converter(100)

def converter2(weight=100):
    ponds=weight/0.45
    print(ponds)

converter2()
converter2(weight=200)
