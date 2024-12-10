n=int(input('N:'))
r=[]
for i in range(n):
    k=int(input())
    r.append(k)
#print(r)
c=int(input('C:'))

def F(num,g):
    min = 10000
    l=len(num)
    if l<4:
        return None

    for i in range(n-3):
        for j in range(i+1,n-2):
            for p in range(j+1,n-1):
                for q in range(p+1,n):
                    v= num[i]+num[j]+num[p]+num[q]
                    d=abs(v-g)
                    if d<min:
                        min=d
                        numbers=[num[i],num[j],num[p],num[q]]
    return numbers,sum(numbers)

print(F(r,c))
