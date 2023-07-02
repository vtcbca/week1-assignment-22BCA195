#[2] Write a python script to enter any number and print the sum of its digit.

def sumofdigit(a):
    b=a
    ram=0
    sum=0
    while(a!=0):
        ram=a%10
        sum=sum+ram
        a//=10
    print(f"The sum of digit of number {b} is {sum}!")  
c=int(input("Enter a number:"))
sumofdigit(c)
