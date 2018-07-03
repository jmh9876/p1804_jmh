#l=[11,22,33,44,22]
#set(l)
#l1=[]
#for i in l:
#    for i not in l1:
#        l1.append(i)
#
class Dan(object):
    __a = None
    def __init__(self):
        pass
    def __new__(cls,*s,**d):
        if cls.__a == None:
            cls.__a = object.__new__(cls,*s,**d)
        return cls.__a
q = Dan()
w = Dan()
print(q)
print(w)
