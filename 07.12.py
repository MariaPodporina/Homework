r=[]
def F(l,n,op,cl):
    if n==num*2:
        r.append(l)
        return
    if op<num:
        F(l+'(',n+1,op+1,cl)
    if op>cl:
        F(l+')',n+1,op,cl+1)
num=int(input())
F('',0,0,0)
print(r)