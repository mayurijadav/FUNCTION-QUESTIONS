# a=["M1y Name is5 Mayuri J4dhav"]
# i=0
# b=""
# c=[]
# while i<(a):
#     j=0
#     while j<(a[i]):
#         if a[i][j]>="A" and a[i][j]<="Z":
#             c.append(a[i][j])
#         j+=1
#     i+=1
#     # c.append(b)
# print(c)





a=["m&y na12me i@s mayu5ri jadhav"]
i=0
while i<len(a):
    j=0
    k=""
    while j<len(a[i]):
        if a[i][j]>="a" and a[i][j]<="z" or a[i][j]==" ":
            k+=a[i][j]
        j=j+1
    i=i+1
print(k)
