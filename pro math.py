import math
def supermath():
    print("welcome to pro math")
    print("================================")
    print("press 1 to calculate the area")
    print("================================")
    print("press 2 to calculate the perimeter")
    print("================================")
    print("press 3 for the calculater")
    print("================================")
    print("press 4 to quit")
    print("================================")
    userchoice1 = int(input("please choose: "))
    # ------------------------ area call
    if userchoice1 == 1:
        print("perimeter calculater")
        print("=================================================================")
        print("press 1 to calculate the area for the square")
        print("=================================================================")
        print("press 2 to calculate the area for the rectangle")
        print("=================================================================")
        print("press 3 to calculate the area for the triangle")
        print("=================================================================")
        print("press 4 to calculate the area for the circle ")
        print("=================================================================")

        userareachoice = int(input("please choose: "))
        #------------------------area shape selector
        #square ↓
        if userchoice1 == 1:
            length = float(input("please enter the length"))
            print("the area of this square is ", length**2)
            again()
            #trinagle ↓
        elif userareachoice ==3:
            base = float(input("please enter the base"))
            length = float(input("please enter the length"))
            print("the area of this triangle is ", .5*base*length)
            again()
            #rectangle ↓
        elif userareachoice ==2:
            length = float(input("please enter the length"))
            base = float(input("please enter the base"))
            print("the area of this rectangle is ", base * length)
            again()
        elif userareachoice ==4:
            Diameter = int(("please enter the Diameter for the circle"))
            print("the area for this circle is " , (math.pi * Diameter))
            again()

        else:
            print("invalid number")
            again()
        # *---------------------------------------
    if userchoice1 == 2:
        print("perimeter calculater")
        print("=================================================================")
        print("press 1 to calculate the perimeter for the square")
        print("=================================================================")
        print("press 2 to calculate the perimeter for the rectangle")
        print("=================================================================")
        print("press 3 to calculate the perimeter for the triangle")
        print("=================================================================")
        print("press 4 to calculate the area for the circle ")
        print("=================================================================")
        userchoice1 = int(input("please choose "))
        if userchoice1 == 1:
            length = float(input("please enter the length"))
            print("the area of this square is ", length*4)
            again()
            #trinagle ↓
        elif userareachoice ==3:
            side1 = float(input("please enter the length for the first side"))
            side2 = float(input("please enter the length for the second side"))
            side3 = float(input("please enter the length for the third side"))
            print("the perimeter of this triangle is ",side1 + side2 + side3 )
            again()
            #rectangle ↓
        elif userareachoice ==2:
            length = float(input("please enter the length"))
            width = float(input("please enter the width"))
            print("the perimeter of this rectangle is ", (base + length)*2)
            again()
        elif userareachoice ==4:
             Diameter1 = float(input("please enter the Diameter"))
             print("the perimeter for this circle is ", math.pi*(Diameter1/2)*2)
        else:
            print("invalid number")
            again()
    if userchoice1 == 3:

        print("free calculater")
        print("==========================================")
        n1 = float(input("please enter you first number "))

        print("press 1 if you want to +")
        print("==========================================")
        print("press 2 if you want to -")
        print("==========================================")
        print("press 3 if you want to /")
        print("==========================================")
        print("press 4 if you want to *")
        print("==========================================")
        print("press 5 if you want to get the square root")
        print("==========================================")
        print("press 6 if you want to get the power")
        callfirt = int(input("please choose the operater "))
        if callfirt == 1:
            n2 = float(input("please enter the second number"))
            print(n1," + ", n2 ,'= ',n1+n2)
            again()
        elif callfirt ==2:
            n2 = float(input("please enter the second number"))
            print(n1," - ", n2 ,'= ',n1-n2)
            again()
        elif callfirt ==3:
            n2 = float(input("please enter the second number"))
            print(n1, " * ", n2, '= ', n1/n2)
            again()
        elif callfirt ==4:
            n2 = float(input("please enter the second number"))
            print(n1," * ", n2 ,'= ',n1*n2)
            again()
        elif callfirt ==6:
            n2 = float(input("please enter the second number"))
            print(n1,'**', n2,'+', n1**n2)
        elif callfirt ==5:
            print("the square root for ",n1 ,"is ", math.sqrt(n1))
            again()
def again():
    yes = input("would you like to try again ? y/n ")
    if yes == 'y':
        supermath()















































































supermath()