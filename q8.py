def check_numbers(a,b):
    for i in range(len(a)):
        if(a[i]%2==0 and b[i]%2==0):
            print("both are even")
        else:
            print("both numbers are not even")
l1=[10,13,20,21,22]
l2=[16,18,19,21,27]
check_numbers(l1,l2)