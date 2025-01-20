r=[]
def f(l,n,op,cl):
    if n==num*2:
        r.append(l)
        return
    if op<num:
        f(l+'(',n+1,op+1,cl)
    if op>cl:
        f(l+')',n+1,op,cl+1)
num=int(input())
f('',0,0,0)
print(r)