# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def add():
    a=(input(" no"))
    i=0
    b=[]
    while i<len(a):
        if "0" not in a[i]:
            b.append(a[i])
        i+=1
    print(b)
add()

