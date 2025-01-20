def f(n,m):
    if n==1 or m==1:
        return 1
    else:
        return f(n-1,m)+f(n,m-1)
n,m=int(input()),int(input())
print(f(n,m))