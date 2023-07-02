# [6]Write a python script to enter any string and print only part of string. Take input of start character and end character from user


def partstring(a):
    st=int(input("Enter start position:"))
    e=int(input("Enter end position:"))
    
    print(f"The part of the string '{a}' is '{a[st-1:e:]}'")

a=input("Enter a string:")
partstring(a)  
