a=input('Строка: ')
if a== "Python":
    print( "ДА")
else:
    print("НЕТ")
b=int(input('Двухзначное число: '))
des=b//10
ed=b%10
if des==ed:
    print("ДА")
else:
    print("НЕТ")
с,d,f=int(input('Число: ')),int(input('Число: ')),int(input('Число: '))
summa=sum(1 for x in [с,d,f] if x%2==0)
print('Колич четных чисел: ',summa)
g=int(input('Число: '))
if 100<=g<1000:
    print("ДА")
else:
    print("НЕТ")
h=int(input('Трехзначное число: '))
sot3=h//100
des3=(h//10)%10
ed3=h%10
if sot3!=des3!=ed3:
    print("Цифры различны")
else:
    print("Цифры не различны")
x,y=int(input('x: ')),int(input('y: '))
if x>0 and y>0:
    print('I')
if x<0 and y>0:
    print('II')
if x<0 and y<0:
    print('III')
if x>0 and y<0:
    print('IV')
i,j,k=int(input('Число: ')),int(input('Число: ')),int(input('Число: '))
if i!=j!=k:
    print('0')
if i==j or j==k or i==k:
    print('2')
if i==j==k:
    print('3')
