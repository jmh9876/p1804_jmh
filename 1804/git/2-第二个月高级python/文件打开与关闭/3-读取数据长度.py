f=open('asd.txt','w')
a=f.write('吕布骑赤兔追貂蝉，董卓骑白龙马杀吕布')
f.close()




f=open('asd.txt','r')
a=f.read(10)
print(a)
print('*'*50)
a=f.read()
print(a)
f.close()
