def car(start=0):
    def tudent():
        nonlocal start
        start +=1
        print(start)
    return tudent

a = car(2)
a()
a()
a()
c = car(3)
c()






print('>'*5)





def student(start=0):
    def father():
        nonlocal start
        start += 1
        print(start)
    return father
a = student(1)
a()
a()
a()
a()
c=student(5)
c()
c()
c()
c()
c()

