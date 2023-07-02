# [4]Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.def armstong(n):


def armstong(a):
    a=int(a)
    rem=0
    sum=0
    b=a
    while(a!=0):
        rem=a%10
        sum=sum+(rem**3)
        a//=10
    if(b==sum):
        print(f"The number {b} is an armstrong number!")
    else:
        print(f"The number {b} is  not an armstrong number!")
        
e=input("Enter a number!!:")
if(e.isdigit()):
    armstong(e)
else:
    print(f"The given input {e} is not valid number!!")
