def factor(a):
    if a==1:
        return 1
    else:
        return(a*factor(a-1))
a=5
c=factor(a)
print(c)