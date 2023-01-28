import math
def zakahsystem():
 print("welcome to Al Zakah project")
 print("=====================")
 print(" press 1 for the Money zakah")
 print("=====================")
 print("press 2 for the cows zakah")
 print("=====================")
 print("press 3 for the sheep zakah")
 print("=====================")
 print("press 4 for the dates zakah")
 print("=====================")
 print("press 5 for the zakat Orud-altejra")
 print("=====================")
 print('press 6 for the zakat alrikaz')
 print("=====================")
 print("press 7 for the silver zakah")
 print("=====================")
 print("press 8 for the gold zakat")
 print("=====================")
 print("note: the digits may be outdated or inaccurate this is for educational purposes only")
 print("=====================")
 user = float(input("please select from the above:"))
 if user == 1:
     zakah = float(input("write the amount of money you have: "))
     if zakah <= 1094.8:
      print("you dont have enough money so you dont need to give out zakah")
      again()
     else:
       print("you need to give out ",zakah/40)
       again()
 if user == 2:
    zakah = float(input("please enter the amount of cows you have: "))
    if zakah <= 30:
        print("you dont have enough cows so you dont need to give out zakah")
        again()
    else:
        print ("you need to give out ",round(zakah / 30))
        again()
 if user == 3:
    zakah = float(input("please enter the amount of sheep you have: "))
    if zakah <= 40:
        print("you dont have enough sheeps so you dont need to give out zakah ")
        again()
    else:
        print("you need to give out ",round(zakah / 40))
        again()
 if user == 4:
    zakah = float(input("please enter the amount of dates you have in kilograms: "))
    if zakah <= 612:
        print("you dont have enough dates so you dont need to give out zakah ")
        again()
    else:
        print("you need to give out ",zakah * 0.05)
        again()
 if user == 5:
    zakah = float(input("please enter the amount of money you got from the business: "))
    if zakah <= 1094.8:
        print("you dont have enough money so you dont need to give out zakah")
        again()
    else:
        print("you need to give out ",zakah * 0.025)
        again()
 if user == 6:
    zakah = float(input("write the please enter the amount of money you got from the rikaz so you dont need to give out zakah "))
    if zakah <= 0:
        print("you dont have enough money")
        again()
    else:
        print("you need to give out ",zakah / 5)
        again()
 if user == 7:
    zakah = float(input("write the amount of silver you have in grams so you dont need to give out zakah "))
    if zakah <= 595:
        print("you dont have enough silver")
        again()
    else:
        print("you need to give out ",zakah *0.025)
        again()
 if user == 8:
    zakah = float(input("write the amount of gold you have in grams: "))
    if zakah <= 80:
        print("you dont have enough gold so you dont need to give out zakah")
        again()
    else:
        print("you need to give out ",zakah *0.025)
        again()
 else:
     print("invalid answer")
     again()
def again():
    again = input("do you want to try again ? y/n")
    if again =='y':
        zakahsystem()
    elif again == 'n' :
        print("thank you for using my program")
zakahsystem()
