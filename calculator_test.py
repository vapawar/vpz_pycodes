#author:vinod pawar

ch = 0
num1=0
num2=0

while ch != 6:
    print "***Calculator***"
    print "1.Addition"
    print "2.Subtraction"
    print "3.Multiplication"
    print "4.Division"
    print "5.Modulus"
    print "6.Exit"
    ch = raw_input("Enter your choice : ")#because user can press enter without any input
    if ch == '':
        ch=0
    else:
        ch=float(ch)#because user can enter float numbers too

    if ch == 1:
        num1 = input ("Enter num1 : ")
        num2 = input ("Enter num1 : ")
        print "The sum of ",num1," and ",num2," is : ",num1 + num2

    elif ch == 2:
        num1 = input ("Enter num1 : ")
        num2 = input ("Enter num1 : ")
        print "The subtraction of ",num2," from ",num1," we get : ",num1 - num2

    elif ch == 3:
        num1 = input ("Enter num1 : ")
        num2 = input ("Enter num1 : ")
        print "The multiplication of ",num1," and ",num2," is : ",num1 * num2

    elif ch == 4:
        num1 = input ("Enter num1 : ")
        num2 = input ("Enter num1 : ")
        print "The dividing  ",num1,"  by  ",num2,"  we get : ",num1 / num2

    elif ch == 5:
        num1 = input ("Enter num1 : ")
        num2 = input ("Enter num1 : ")
        print "Modula of ",num1," by ",num2," is ",num1 % num2

    elif ch == 6:
        exit(0)

    else:
        print "try again...........\n"
        continue
