def car(a,b):
    def way(x):
        nonlocal a
        print('y = %d * %d + %d'%( a , x , b))
        a += 1
        y = a * x + b
        return y
    return way
w = car(2,4)
print(w(3))

