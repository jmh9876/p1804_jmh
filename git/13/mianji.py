list=[{'北京':{'面积':'1000平','人口':'200w'},'上海':{'面积':'600平','人口':'150w'}}]
for i in list:
    for a,s in i.items():
        for d,f in s.items():
            print(a,d,f)
