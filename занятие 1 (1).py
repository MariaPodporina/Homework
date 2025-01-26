a=int(input('двухзначнре число '))
des=a//10
ed=a%10
sum=des+ed
swap=str(ed)+str(des)
b=int(input('трехзначное число '))
sot3=b//100
des3=b//10%10
ed3=b%10
print(f'1.1 Десятков: {des} Единиц: {ed}')
print(f'1.2 Сумма:{sum}')
print(f'1.3 Перестановка: {swap}')
print(f'1.4 Цифры числа: {sot3},{des3},{ed3}')
