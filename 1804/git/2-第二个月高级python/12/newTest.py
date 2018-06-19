class Car(object):
    def __init__(self):
        #print(self)
        print('狮子在吼叫~~~~~~~~~~~~~~')
    def __new__(cls,*a):
        #print(id(cls))
        print('狮子在称王~~~~~~~~~~~~')
        return object.__new__(cls)
Car()
#a=Car()
#print(a)
print(id(Car))
