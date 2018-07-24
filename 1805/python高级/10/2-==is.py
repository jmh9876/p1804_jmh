import copy

a = (1,2)

b = (3,4)

c = (a,b)

d = copy.deepcopy(c)

id(d) == id(c)
True

a = [1,2]

b = [3,4]

c = [a,b]

d = copy.deepcopy(c)

id(d) == id(c)
False

