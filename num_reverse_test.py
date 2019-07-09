#author:vinod pawar

num=0
rev=0
rem=0

num=raw_input("Enter any number : ")

while num>0:
    rem=num%10
    num=num/10
    rev=rem+rev*10

print ("The reverse is ",rev)
raw_input("Press return to exit....")
