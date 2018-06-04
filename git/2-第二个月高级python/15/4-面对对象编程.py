stu_a={
       'name':'A',
       'age':21,
       'gender':1,
       'hometown':'河南'
}
stu_b={
       'name':'B',
       'age':22,
       'gender':0,
       'hometown':'山东'
}
stu_c={
       'name':'C',
       'age':20,
       'gender':1,
       'hometown':'安徽'
}
def stu_intro(stu):
    '''自我介绍'''
    for key,value in stu.items():
        pritn('key=%s,value=%d'%(key,value))
stu_intro(stu_a)
stu_intro(stu_b)
stu_intro(stu_c)
