# [7]Write a python script to enter any string, replace vowel with its position number.
#For Example: input: Amit
#            output:0m2t


def vowelchange(e):
    b=''
    a=('a','e','i','o','u','A','E','I','O','U')
    for index,j in enumerate(e):
        if(j in a):
            b+=str(index)
        else:
            b+=j   
    print(f"The string '{e}' after change is '{b}' ")
e=input("Enter a string:")
vowelchange(e)
