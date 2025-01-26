banks = int(input('Количество банков '))
r = []
for _ in range(banks):
    name = input('Название ')
    money = int(input('Колич денег '))
    no = int(input('Номер '))
    bank = (name, money, no)
    r.append(bank)

k=0
result = []
for x, y, z in r:
    for h, l, v in r:
        if abs(z - v) > 1:
            y = ((y + l), (x, z), (h, v))
            result.append(y)
for i, j, u in result:
    k=max(i,k)
for i, j, u in result:
    if i == k:
        print([i, j, u])
        break
    else:
        continue
