import os
import time
clear = lambda: os.system('cls')

# Get Price from user
def Get_Price():
    while True:
        price = raw_input("Give max price for car : \n")
        if price ==" ":
            print " You have to give something"
            continue
        try:
            pricing = int(price)
            return pricing
        except:
            print " Give an integer"
            continue

# Get Market Filers from user
def Get_Market_Filters():
    while True:
        filters = {1:"&condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF",
                   2:"&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF",
                   3:"&offer_type=sale",
                   4:"&offer_type=wanted",
                   5:"&offer_type=rent"}
        f = []
        fa = []
        while True:
            if len(f)==5:
                print "\n- All filters are selected -"
                break
            clear()
            print "You have "+str(len(f))+" filters"
            print "Filters :"
            print "  1 - kainourgio"
            print "  2 - metaxeirismeno"
            print "  3 - pwleitai"
            print "  4 - zhteitai"
            print "  5 - enoikiazetai"
            if len(f)==0:
                print "  6 - no filter"
            else:
                print "  6 - finished with the filters"
            while True:
                i = raw_input()
                if i==" ":
                    print " You have to give something"
                else:
                    break
            if i in fa:
                print " Give filter's code only once"
                time.sleep(2)
                continue
            if i=="6":
                break
            try:
                f.append(str(filters[int(i)]))
                fa.append(i)
            except:
                print "Input must be : 1 or 2 or 3 or 4 or 5"
                time.sleep(2)
                continue 
            while True:
                cont = raw_input("Add more filters ? ( yes / no )\n")
                if cont==" ":
                    print " You have to give something"
                else:
                    break
            if cont[0]=="Y" or cont[0]=="y":
                continue
            elif cont[0]=="N" or cont[0]=="n":
                break
        break
    return f
