# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def case():
    b="The quick Brow Fox"
    i=0
    count=0
    count1=0
    c=[]
    d=[]
    while i<len(b):
        if b[i]>="A" and b[i]<="Z":
            c.append(b[i])
            count+=1
        elif b[i]>="a" and b[i]<="z":
            d.append(b[i])
            count1+=1
        i+=1
    print(count,c)
    print(count1,d)
case()

# def case():
#     b="The quick Brow Fox"
#     i=0
#     count=0
#     count1=0
#     while i<len(b):
#         if b[i]>="A" and b[i]<="Z":
#             count+=1
#         elif b[i]>="a" and b[i]<="z":
#             count1+=1
#         i+=1
#     print(count)
#     print(count1)
# case()