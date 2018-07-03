l = []
s = []
for i in range(100):
    l.append(i)
l = iter(l)
n = 0
a,b = 0,1
while n < 100:
    s.append(b)
    a,b = b,a+b
    n += 1
for i in l:
    if i in s:
        print(i)
