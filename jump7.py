a=0
b=0
while a<100:
    a+=1
    b=str(a).find('7')
    if b!=-1 or a%7==0:
        continue
    else:
        print(a)
