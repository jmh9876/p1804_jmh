a=1

while a<=9:
    s=1
    while s<=a:
        print('%d*%d=%d'%(s,a,a*s),end='\t')
        s+=1
    print('')
    a+=1
