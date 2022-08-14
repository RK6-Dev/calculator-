cart = []
total = 0
def again():
    again = input("would you like to shop again ? y/n ")
    if again == 'y':
        shop()
    elif again == 'n':
        print("thank you for using my program")
    else:
        print("invalid choice")
        again
def line():

    print("==========================================")
def shop():


    def afterchoice(name, price, total = 0):
        cart.append(name)
        total += (price)
        print("you added", name, "to your cart  ")
        print('----------------------------')
        print("press 1 to continue shopping")
        print('----------------------------')
        print("press 2 to checkout")
        print('----------------------------')
        after_add = int(input("please choose an option"))
        if after_add == 2:
            print("you cart have ", cart)
            print("you total is ", str(total))
            again()
        elif after_add == 1:
            shop()
    # categories menu↓
    name = input("please enter you name: ")
    print("welcome ", name, "to the shop ")
    line()
    print("press 1 for phones")
    line()
    print("press 2 for gaming consoles")
    line()
    print("press 3 for television")
    line()
    print("press 4 for laptops")
    line()
    print("press 5 to quit")
    line()
    # ↓ category choice
    category_choice = int(input("please choose one from the above :"))
    # -----------------------------------------------------------------------------------
    # phones section ↓
    if category_choice == 1:
        print("phones section")
        line()
        print("press 1 for iphones")
        line()
        print("press 2 for Smasung phones")
        line()
        print("press 3 for huawei")
        line()
        print("press 4 to quit")
        line()
        # phone brand user choice ↓
        phone_brand = int(input("please choose one from the above: "))
        #iphones ↓
        if phone_brand == 1:
            print("iphone section")
            line()
            print("press 1 for iphone 13")
            line()
            print("press 2 for iphone 12")
            line()
            print("press 3 for iphone 11")
            line()
            print("press 4 to quit")
            line()
            iphone_model = int(input("please choose one from the above: "))
            line()
            # ------------------
            # iphone 13 ↓
            if   iphone_model == 1:
                print("iphone 13 section")
                line()
                print("press 1 for iphone 13 pro max  price:5966 sar")
                line()
                print("press 2 for iphone 13 pro      price:5199 sar")
                line()
                print("press 3 for iphone 13          price:4299 sar")
                line()
                print("press 4 to iphone 13 mini      price:3799 sar")
                line()
                print("note: all the phones are 256 gb")
                line()
                print("press 5 to quit")
                line()
                iphone_13 = int(input("please choose from the above: "))
                if iphone_13 == 1:
                    afterchoice("iphone 13 pro max", 5966, total)
                elif iphone_13 == 2:
                    afterchoice("iphone 13 pro",5199, total)
                elif iphone_13 == 3:
                    afterchoice("iphone 13 ", 4299, total)
                elif iphone_13 == 4:
                    afterchoice("iphone 13 mini", 3799, total)
                elif iphone_13 == 5:
                    print("thank you for using my program")
                else:
                    print("invalid choice")
                    again()
            # iphone 12 ↓
            elif iphone_model == 2:
                print("iphone 12 section")
                line()
                print("press 1 for iphone 12 pro max  price:5199 sar")
                line()
                print("press 2 for iphone 12 pro      price:4799 sar")
                line()
                print("press 3 for iphone 12          price:3299 sar")
                line()
                print("press 4 to iphone 12 mini      price:2999 sar")
                line()
                print("note: all the phones are 256 gb")
                line()
                print("press 5 to quit")
                line()
                iphone_13 = int(input("please choose from the above: "))
                if iphone_13 == 1:
                    afterchoice("iphone 12 pro max", 5199, total)
                elif iphone_13 == 2:
                    afterchoice("iphone 12 pro",4799, total)
                elif iphone_13 == 3:
                    afterchoice("iphone 12 ", 3299, total)
                elif iphone_13 == 4:
                    afterchoice("iphone 12 mini", 2999, total)
                elif iphone_13 == 5:
                    print("thank you for using my program")
                else:
                    print("invalid choice")
                    again()
            # iphone 11 ↓
            elif iphone_model == 3:
            #iphone 11 ↓
                print("iphone 11 section")
                line()
                print("press 1 for iphone 11 pro max  price:4399 sar")
                line()
                print("press 2 for iphone 11 pro      price:3629 sar")
                line()
                print("press 3 for iphone 11          price:2299 sar")
                line()
                print("note: all the phones are 128 gb")
                line()
                print("press 4 to quit")
                line()
                iphone_13 = int(input("please choose from the above: "))
                if iphone_13 == 1:
                    afterchoice("iphone 11 pro max", 4399, total)
                elif iphone_13 == 2:
                    afterchoice("iphone 11 pro",3629, total)
                elif iphone_13 == 3:
                    afterchoice("iphone 11 ", 2299, total)
                elif iphone_13 == 4:
                    print("thank you for using my program")
                else:
                    print("invalid choice")
                    again()
        # samsung phones ↓
        elif phone_brand == 2:
            print("samsung section")
            line()
            print("press 1 for galaxy fold")
            line()
            print("press 2 for galaxy s")
            line()
            print("press 3 for galaxy note")
            line()
            print("press 4 to quit")
            line()
            samsung_model = int(input("please choose one from the above: "))
            line()
            # ------------------
            # zfold models ↓
            if samsung_model == 1:
                print("press 1 for galaxy fold 3   price:6799 sar")
                line()
                print("press 2 for galaxy fold 2   price 5299 sar")
                line()
                print("note: galaxy fold 1 is discontinued")
                line()
                print("press 3 to exit")
                line()
                # zfold use choice  ↓
                fold = int(input("please choose from the above"))
                if fold == 1 :
                    afterchoice("galaxy fold 3", 6752, total)
                elif fold == 2:
                    afterchoice("galaxy fold 2", 5299, total)
                elif fold == 3:
                    print("thank you for using my program")
            # s models ↓
            elif samsung_model == 2:
                print("press 1 for galaxy s22 ultra   price:4899 sar")
                line()
                print("press 2 for galaxy s22 plus   price:3999 sar")
                line()
                print("press 3 for galaxy s22        price:3099 sar")
                line()
                print("press 4 to exit")
                line()
                # s22 user choice ↓
                s22 = int(input("please choose from the above"))
                if s22 == 1:
                     afterchoice("galaxy s22 ultra", 4899, total)
                elif s22 == 2:
                     afterchoice("galaxy s22 plus", 3999, total)
                elif s22 == 3 :
                    afterchoice("galaxy s22", 3099, total)
                elif s22 == 4:
                    print("thank you for using my program")
                else:
                    print("invalid number")
                    again()
            # note models ↓
            elif samsung_model == 3:
                print("press 1 for galaxy note 20 ultra   price:3184 sar")
                line()
                print("press 2 for galaxy note 20         price:2599 sar")
                line()
                print("press 3 to exit")
                line()
                # s22 user choice ↓
                s22 = int(input("please choose from the above"))
                if s22 == 1:
                     afterchoice("galaxy note 20 ultra ultra", 3184, total)
                elif s22 == 2:
                     afterchoice("galaxy s22 plus", 2599, total)
                elif s22 == 3:
                    print("thank you for using my program")
                else:
                    print("invalid number")
                    again()
        # huawei phone ↓
        elif phone_brand == 3:
            print("huawei section")
            line()
            print("press 1 for huawei p")
            line()
            print("press 2 for huawei mate")
            line()
            print("press 3 to quit")
            line()
            huawei_model = int(input("please choose one from the above: "))
            line()
            if huawei_model == 1:
                print("press 1 for huawei p50 pro    price:3499 sar")
                line()
                print("press 2 for huawei p50        price:2599 sar")
                line()
                print("press 3 fpr huawei p40 pro    price:2999 sar")
                line()
                print("press 4 for huawei p40        price:2596 sar ")
                line()
                print("press 5 to exit")
                line()
                # huawei p50 /40 user choice  ↓
                p = int(input("please choose from the above"))
                if p == 1 :
                    afterchoice("huawei p50 pro ", 3499, total)
                elif p == 2:
                    afterchoice("huawei p50  ", 2599, total)
                elif p == 3:
                    afterchoice("huawei p40 pro ", 2999, total)
                elif p == 4:
                    afterchoice("huawei p40 ", 2596, total)
                elif p ==5:
                    print("thank you for using my program")
                else:
                    print("invalid input")
                    again()
            elif huawei_model == 2:
                print("press 1 for huawei mate Xs 2     price:7999 sar")
                line()
                print("press 2 for huawei mate 40 pro   price:4388 sar")
                line()
                print("press 3 to exit")
                line()
                # huawei mate user choice  ↓
                mate = int(input("please choose from the above"))
                if mate == 1 :
                    afterchoice("huawei mate Xs 2", 7999, total)
                elif mate == 2:
                    afterchoice("huawei mate 40 pro ", 4388, total)
                elif mate ==3:
                    print("thank you for using my program")
                else:
                    print("invalid input")
                    again()
    elif category_choice == 2:
        #ps or xbox ↓
        print("gaming consoles section")
        line()
        print("press 1 for xbox")
        line()
        print("press 2 for playstation")
        line()
        console = int(input("please choose from the above: "))
        if console == 1 :
        #xbox
            print("xbox section")
            line()
            print("press 1 for xbox 1")
            line()
            print("press 2 for xbox series")
            line()
            xbox_modle = int(input("please choose from the above: "))
            if xbox_modle == 1:
                # xbox 1 ↓
                print("xbox 1 section")
                line()
                print("press 1 for xbox 1 x     price: 1699 sar")
                line()
                print("press 2 for xbox one s   price: 1599 sar")
                line()
                print("press 3 to exit")
                # xbox 1 user choice
                xbox1 = int(input("please choose from the above: "))
                if xbox1 == 1:
                    afterchoice("xbox 1 x  ", 1699, total)
                elif xbox1 ==2:
                    afterchoice("xbox 1 s  ", 1599, total)
                elif xbox1 == 3:
                    print("thank you for using my program")
                else:
                    print("invalid choice ")
                    again()
            elif xbox_modle == 2:
                # xbox series ↓
                print("xbox series section")
                line()
                print("press 1 for xbox series x     price: 2226 sar")
                line()
                print("press 2 for xbox series s   price: 1294 sar")
                line()
                print("press 3 to exit")
                # xbox series user choice
                xboxseries = int(input("please choose from the above: "))
                if xboxseries == 1:
                    afterchoice("xbox series x  ", 2226, total)
                elif xboxseries == 2:
                    afterchoice("xbox series s  ", 1294, total)
                elif xboxseries == 3:
                    print("thank you for using my program")
                else:
                    print("invalid choice ")
                    again()
        elif console == 2:
            # playstation
            print("playstation section")
            line()
            print("press 1 for playstation 5")
            line()
            print("press 2 for playstation 4")
            line()
            playstation_modle = int(input("please choose from the above: "))
            if playstation_modle == 1:
                #  1 ↓
                print("xbox 1 section")
                line()
                print("press 1 for playstation 4 pro    price: 1828 sar")
                line()
                print("press 2 for playstation 4        price: 1379 sar")
                line()
                print("press 3 to exit")
                # ps user choice
                ps = int(input("please choose from the above: "))
                if ps == 1:
                    afterchoice("xbox 1 x  ", 1699, total)
                elif ps == 2:
                    afterchoice("xbox 1 s  ", 1599, total)
                elif ps == 3:
                    print("thank you for using my program")
                else:
                    print("invalid choice ")
                    again()
            elif playstation_modle == 2:
                # ps5 ↓
                print("xbox series section")
                line()
                print("press 1 for playstation 5 disk      price: 3239 sar")
                line()
                print("press 2 for playstation 5 digital   price: 2829 sar")
                line()
                print("press 3 to exit")
                # ps5 user choice
                ps5 = int(input("please choose from the above: "))
                if ps5 == 1:
                    afterchoice("xbox series x  ", 3239, total)
                elif ps5 == 2:
                    afterchoice("xbox series s  ", 2829, total)
                elif ps5 == 3:
                    print("thank you for using my program")
                else:
                    print("invalid choice ")
                    again()
    elif category_choice == 3:
        # Tv brand user choice ↓
        print("tv section")
        line()
        print("press 1 for lg")
        line()
        print("press 2 for Smasung ")
        line()
        print("press 3 to quit")
        line()
        Tv_brand = int(input("please choose one from the above: "))
        #lg model menu
        if Tv_brand == 1:
            print("lg section ")
            line()
            print("press 1 for  LG 83 4K OLED TV, Smart TV,          price: 17999sar")
            line()
            print("press 2 for LG 88 Inch, 8K OLED TV, Smart TV      price:72000sar ")
            line()
            print("press 3 for LG 75 Inch, 8K QNED MiniLED TV,       price:9999sar ")
            line()
            print("press 4 to exit ")

            # lg user choice  ↓
            lg = int(input("please choose from the above"))
            if lg == 1:
                afterchoice("LG 83 4K OLED TV, Smart TV,", 17999, total)
            elif lg == 2:
                afterchoice("LG 88 Inch, 8K OLED TV, Smart TV", 72000, total)
            elif lg == 3:
                afterchoice("LG 75 Inch, 8K QNED MiniLED TV", 9999, total)
            elif lg == 4:
                print("thank you for using my program")
        #Samsung tv menu ↓
        elif Tv_brand == 2:
            print("Samsung section ")
            line()
            print("press 1 for  Samsung, 75 Inch, Frame TV, QLED 4K HDR, Smart TV,          price: 12499sar")
            line()
            print("press 2 for Samsung, 75 Inch, 4K Smart TV,                               price:7499sar ")
            line()
            print("press 3 for Samsung, 32 Inch, FHD Smart TV,                              price:1349sar ")
            line()
            print("press 4 to exit ")

            # lg user choice  ↓
            lg = int(input("please choose from the above"))
            if lg == 1:
                afterchoice("Samsung, 75 Inch, Frame TV, QLED 4K HDR, Smart TV", 12499, total)
            elif lg == 2:
                afterchoice("Samsung, 75 Inch, 4K Smart TV", 7499, total)
            elif lg == 3:
                afterchoice("Samsung, 32 Inch, FHD Smart TV,", 1349, total)
            elif lg == 4:
                print("thank you for using my program")
    elif category_choice == 4:
        print("laptops section")
        line()
        print("press 1 for dell laptops")
        line()
        print("press 2 for msi laptops")
        line()
        print("press 3 for hp laptops")
        line()
        print("press 4 to quit")
        line()
        laptop_brand = int(input("please choose one from the above: "))
        #dell↓
        if laptop_brand == 1:
            print("dell section")
            line()
            print("press 1 for  dell XPS laptops")
            line()
            print("press 2 for  dell inspiron laptops")
            line()
            print("press 3 for  dell G laptops")
            line()
            print("press 4 to exit")
            line()
            dell_model = int(input("please choose one from the above: "))

            #dell xps ↓
            if dell_model == 1:
                print("dell XPS section")
                line()
                print("press 1 for  dell XPS 13 laptop     price:4999 sar")
                line()
                print("press 2 for  dell XPS 15 9520 laptop     price:9999")
                line()
                print("press 3 to exit")
                line()
                xps_model = int(input("please choose one from the above: "))
                if xps_model == 1:
                    afterchoice("dell XPS 13 laptop  ", 4999, total)
                elif xps_model == 2:
                    afterchoice("dell XPS 15 9520 laptop ", 9999, total)
                elif xps_model == 3:
                    print("thank you for using my program")
            #dell inspiron↓
            elif dell_model == 2:
                print("dell inspiron section")
                line()
                print("press 1 for  dell inspiron 15 3511 laptop     price:3699 sar")
                line()
                print("press 2 for  dell inspiron 14 5410 laptop     price:3499")
                line()
                print("press 3 to exit")
                line()
                xps_model = int(input("please choose one from the above: "))
                if xps_model == 1:
                    afterchoice("dell inspiron 15 3511 laptop  ", 3699, total)
                elif xps_model == 2:
                    afterchoice("dell inspiron 14 5410 laptop ", 3499, total)
                elif xps_model == 3:
                    print("thank you for using my program")
            #dell vostro ↓
            elif dell_model == 3:
                print("dell G section")
                line()
                print("press 1 for  dell G15 5515 laptop     price:5199 sar")
                line()
                print("press 2 for  dell G14 5511 laptop     price:4599")
                line()
                print("press 3 to exit")
                line()
                xps_model = int(input("please choose one from the above: "))
                if xps_model == 1:
                    afterchoice("dell G15 5515 laptop  ", 5199, total)
                elif xps_model == 2:
                    afterchoice("dell G14 5511 laptop ", 4599, total)
                elif xps_model == 3:
                    print("thank you for using my program")
        elif laptop_brand == 2:
            print("msi section")
            line()
            print("press 1 for MSI GF66 Katana 12UE Gaming Laptop     price:7099 sar")
            line()
            print("press 2 for MSI Modern 14 B5M Laptop               price:2699 sar")
            line()
            print("press 3 for MSI GS66 Stealth 12UGS Gaming Laptop   price:12199 sar")
            line()
            print("press 4 to exit")
            line()
            msi_model = int(input("please choose one from the above: "))
            if msi_model == 1:
                afterchoice("MSI GF66 Katana 12UE Gaming Laptop  ", 7099, total)
            elif msi_model == 2:
                afterchoice("MSI Modern 14 B5M Laptop ", 2699, total)
            elif msi_model == 3:
                afterchoice("MSI GS66 Stealth 12UGS Gaming Laptop ", 12199, total)
            elif msi_model == 4:
                print("thank you for using my program")
        elif laptop_brand == 3:
            print("hp section")
            line()
            print("press 1 for HP 15-dw3070nx Laptop                price:2999 sar")
            line()
            print("press 2 for HP ENVY 13-ba1008nx Laptop           price:5499 sar")
            line()
            print("press 3 for HP OMEN 16-c0009nx Gaming Laptop     price:7399 sar")
            line()
            print("press 4 to exit")
            line()
            hp_model = int(input("please choose one from the above: "))
            if hp_model == 1:
                afterchoice("HP 15-dw3070nx Laptop  ", 2999, total)
            elif hp_model == 2:
                afterchoice("HP ENVY 13-ba1008nx Laptop ", 5499, total)
            elif hp_model == 3:
                afterchoice("HP OMEN 16-c0009nx Gaming Laptop ", 7399, total)
            elif hp_model == 4:
                print("thank you for using my program")



shop()

