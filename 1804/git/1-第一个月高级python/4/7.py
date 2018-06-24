renwu=1
while renwu<=3:
    if renwu==1:
        print('快去签到%d'% renwu)
    elif renwu==2:
        print('快去采草药%d'% renwu)
        caoyao=0

        while caoyao<10:
            #if caoyao==renwu:
            print('弯腰，采药')
            caoyao=caoyao+1
    else:
        print('快去找小红帽%d'% renwu)
    renwu+=1
