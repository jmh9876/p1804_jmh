import random
l=[]
class Shu():
    def su(self):
        number = random.randint(1,101)
        for number in range(10):
            if number == number:
                number = random.randint(1,101)
                l.append(number)
        print(l)
xiao = Shu()
xiao.su()
