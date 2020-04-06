try:
    print(10/6)
    print(10+'0')
#except:
    #print('you can not do it')
except ArithmeticError as e:
    print(e)
#except TypeError as e:
#    print(e)
except Exception:
    print('there is something wrong')


