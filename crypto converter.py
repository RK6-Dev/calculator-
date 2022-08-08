print("welocme to the crypto curreny convertor")
userinput = 0

print("--------------------------------------------------")

print("please press 1 if you want to convert from crypto to usd")
print("please press 2 if you want to convert from usd  to crypto")
print("---------------------------------------------------------- "
      "")
userchoice = int(input())

if userchoice == 1:
    print("----------------------------------------------------------------------------")
    print("press 1 if you want to convert from bitcoin to usd")
    print("press 2 if you want to convert from ethereum to usd")
    print("press 3 if you want to convert from bnb to usd")
    print("press 4 if you want to convert from solona to usd")
    print("press 5 if you want to convert from cordano to usd ")
    print("press 6 if you want to convert from dogecoin to usd")
    print("press 7 if you want to convert from shiba inu to usd")
    print("press 8 if you want to convert from litecoin to usd")
    print("press 9 if you want to convert from maker to usd")
    print("press 10 if you want to convert from compound to usd")
    print("press 11 if you want to exit ")

    usecurrency = float(input("please enter the amount you have in crypto "))

    userinput = int(input("please chose the currency you want to conver "))
    if userinput == 1:
        bitcoin = usecurrency * 22851.78
        print((usecurrency), "bitcoin ", "in usd = ", bitcoin, "$")
    if userinput == 2:
        eth = usecurrency * 1618.35
        print((usecurrency), "eth ", "in usd = ", eth, "$")
    if userinput == 3:
        bnb = usecurrency * 282.68
        print((usecurrency), "bnb ", "in usd = ", bnb, "$")
    if userinput == 4:
        solona = usecurrency * 38.34
        print((usecurrency), "solona ", "in usd = ", solona, "$")
    if userinput == 5:
        cordano = usecurrency * 0.5004
        print((usecurrency), "cordano ", "in usd = ", cordano, "$")
    if userinput == 6:
        dogecoin = usecurrency * 0.06646
        print((usecurrency), "doge ", "in usd = ", dogecoin, "$")
    if userinput == 7:
        shiba = usecurrency * 0.00001177
        print((usecurrency), "shiba", "in usd = ", shiba, "$")
    if userinput == 8:
        litecoin = usecurrency * 57.55
        print((usecurrency), "lite ", "in usd = ", litecoin, "$")
    if userinput == 9:
        make = usecurrency * 1042.17
        print((usecurrency), "maker ", "in usd = ", make, "$")
    if userinput == 10:
        compund = usecurrency * 56.89
        print((usecurrency), "in usd = ", compund, "$"
              )
    if userinput == 11:
        print("thank you for using my program")

if userchoice == 2:

    print("----------------------------------------------------------------------------")
    print("press 1 if you want to convert from usd to bitcoin")
    print("press 2 if you want to convert from usd to ethereum")
    print("press 3 if you want to convert from usd to bnb")
    print("press 4 if you want to convert from usd to solona")
    print("press 5 if you want to convert from usd to cordano  ")
    print("press 6 if you want to convert from usd to dogecoin")
    print("press 7 if you want to convert from usd to shiba ")
    print("press 8 if you want to convert from usd to litecoin")
    print("press 9 if you want to convert from usd to  maker")
    print("press 10 if you want to convert from usd to compound ")
    print("press 11 if you want to exit ")
    usecurrency = float(input("pelase enter your balance in usd"))
    userinputt = int(input("please choose the currency you want to convert"))

    if userinputt == 1:
        bitcoin = usecurrency / 22851.78
        print((usecurrency), "$ ", "  in bitcoin = ", bitcoin)
    if userinputt == 2:
        eth = usecurrency / 1618.35
        print((usecurrency), "$ ", "in eth = ", eth)
    if userinputt == 3:
        bnb = usecurrency / 282.68
        print((usecurrency), "$ " "in  bnb= ", bnb)
    if userinputt == 4:
        solona = usecurrency / 38.34
        print((usecurrency), "$ ""in solona = ", solona)
    if userinputt == 5:
        cordano = usecurrency / 0.5004
        print((usecurrency), "$ " "in cordano = ", cordano)
    if userinputt == 6:
        dogecoin = usecurrency / 0.06646
        print((usecurrency), "$ " "in doge= ", dogecoin)
    if userinputt == 7:
        shiba = usecurrency / 0.00001177
        print((usecurrency), "$ " "in shiba = ", shiba)
    if userinputt == 8:
        litecoin = usecurrency / 57.55
        print((usecurrency), "$ " "in lite = ", litecoin)
    if userinputt == 9:
        make = usecurrency / 1042.17
        print((usecurrency), "$ " "in maker = ", make)
    if userinputt == 10:
        compund = usecurrency / 56.89
        print((usecurrency), "$  " "in compound = ", compund
              )
    if userinputt == 11:
        print("thank you for using my program")

    # -----------
