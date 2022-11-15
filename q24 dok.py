# Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting
# to be 18. )

def add():
    age=int(input("enter no"))
    if age>=18:
        print("he/she can vote")
    else:
        print("he\she can not vote")
add()