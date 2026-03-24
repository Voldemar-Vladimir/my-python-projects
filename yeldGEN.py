def countdown(n):
    while n>=0:
        yield n
        n-=1
d=countdown(n=6)
print(next(d))