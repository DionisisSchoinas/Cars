import os
import time
clear = lambda: os.system('cls')


# Get Min Price from user
def Get_Price_Min():
    while True:
        clear()
        price = raw_input("Give min price for car ( 0 for no filter ) : \n")
        if price ==" ":
            print " You have to give something"
            time.sleep(2)
            continue
        elif price=="0":
            return price
        try:
            price = int(price)
            return price
        except:
            print " Give an integer"
            time.sleep(2)
            continue
        break

# Get Min Price from user
def Get_Price_Max(start):
    while True:
        clear()
        price = raw_input("Give max price for car ( 0 for no filter ) : \n")
        if price ==" ":
            print " You have to give something"
            time.sleep(2)
            continue
        elif price=="0":
            a = 1000000
            return a
        try:
            price = int(price)
            if price < start:
                print " Max price can't be lower than min price"
                time.sleep(2)
                continue
            return price
        except:
            print " Give an integer"
            time.sleep(2)
            continue
        break

# Get Starting Year from user
def Get_Starting_Year():
    while True:
        clear()
        date = raw_input("Give starting year for search ( ex. 1950 ) ( 0 for no filter ) : \n")
        if date ==" ":
            print " You have to give something"
            time.sleep(2)
            continue
        elif date=="0":
            return "1800"
        elif len(date)!=4:
            print " Date must be 4 numbers ( ex. 1949 )"
            time.sleep(2)
            continue
        return date

# Get Ending Year from user
def Get_Ending_Year(start):
    while True:
        clear()
        date = raw_input("Give ending year for search ( ex. 1990 ) ( 0 for no filter ) : \n")
        if date ==" ":
            print " You have to give something"
            time.sleep(2)
            continue
        elif date=="0":
            return "3000"
        elif len(date)!=4:
            print " Date must be 4 numbers ( ex. 1998 )"
            time.sleep(2)
            continue
        elif start > date:
            print " Ending year can't be before starting year"
            time.sleep(2)
            continue
        return date

# Get Market Filters from user
def Get_Market_Filters():
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
        if cont[0].upper()=="Y":    
            continue    
        elif cont[0].upper()=="N":    
            break       
    return f

# Get Category filters from user
def Get_Category():
    filters = {1:"&category=18",
               2:"&category=664",
               3:"&category=14",
               4:"&category=485",
               5:"&category=665",
               6:"&category=12",
               7:"&category=15",
               8:"&category=11",
               9:"&category=10",
               10:"&category=13",
               11:"&category=16"}
    f=[]
    fa=[]
    while True:
        if len(f)==11:
            print "\n- All filters are selected -"
            break        
        clear()
        print "You have "+str(len(f))+" filters"
        print "Filters :"
        print "  1 - 4x4 / Jeep"
        print "  2 - Van / Mini Bus"    
        print "  3 - Agrotiko"    
        print "  4 - Agwnistiko"    
        print "  5 - Epaggelmatiko Epivatiko"    
        print "  6 - Kabrio"
        print "  7 - Koupe"
        print "  8 - Compact"
        print "  9 - Kobi / Karavan"
        print "  10 - Limouzina"
        print "  11 - Allo"
        if len(f)==0:    
            print "  12 - no filter"  
        else:    
            print "  12 - finished with the filters"
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
        if i=="12":    
            break    
        try:    
            f.append(str(filters[int(i)]))    
            fa.append(i)    
        except:    
            print "Input must be between 1-12"    
            time.sleep(2)    
            continue     
        while True:    
            cont = raw_input("Add more filters ? ( yes / no )\n")    
            if cont==" ":    
                print " You have to give something"    
            else:    
                break    
        if cont[0].upper()=="Y":    
            continue    
        elif cont[0].upper()=="N":    
            break 
    return f       
