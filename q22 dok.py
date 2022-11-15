# Q14.Write a function to check if a number is prime or not.


def prime():
    a=int(input("enter prime number"))
    b=int(input("enter no"))
    if a%b!=0 and a%a==0 and a%1==0:
        print("prime no hai")
    else:
        print("not a prime number")
prime()
 