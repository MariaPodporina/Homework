def labirint(n,m):
    if n==1 or m==1:
        return 1
    else:
        return labirint(n-1,m)+labirint(n,m-1)
n,m=int(input()),int(input())
print(labirint(n,m))