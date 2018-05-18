list_card=['wangwu',20,'nan']
a=100
def tast1():
    global a
    a+=1
    print(a)
    list_card[2]='nv'
    list_card.append('001')
    print(list_card)
def tast2():
    print(a)
tast2()
tast1()



list_cad=['zhangbin',18,'nan']
s=200
def asd():
    global s
    s+=1
    print(s)
    list_cad[1]=20
    list_cad.append('001')
    print(list_cad)
def asd1():
    print(s)
asd()
asd1()
