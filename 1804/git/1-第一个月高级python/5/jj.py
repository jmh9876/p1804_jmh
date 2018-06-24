a=1
while a<=9:
    s=1
    while s<=a:
        print('%d*%d=%d'%(s,a,s*a),end='\t')
        s=s+1
    print('')
    a=a+1
