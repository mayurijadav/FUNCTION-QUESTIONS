# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def add():
    list=[1,2,4,5,6,7,8,9]
    i=0
    a=[]
    while i<len(list):
        if list[i]%2==0:
            a.append(list[i])
        i+=1
    print(a)
add()