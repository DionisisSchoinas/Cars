import os
import time
clear = lambda: os.system('cls')

# Complete dictionary for brand
def Fill_Dictionary(data,dictionary_mark):
    # Get code
    start0 = data.find('<ul class="facets-multi-select-container makes-list">')
    for i in range(142):
        start = start0
        str1 = '<input autocomplete="off" type="checkbox" name="make" '
        start1 = data[start:].find(str1) + 8
        end = data[start+start1+len(str1):].find('"')
        code = data[start+start1+len(str1):start+start1+len(str1)+end]
        # Get mark
        start_mark = start+start1+len(str1)+end
        start = start_mark
        str1 = '<span class="multi-select-option-name">'
        start1 = data[start:].find(str1) + len(str1)
        end = data[start+start1:].find('</span>')
        mark = data[start+start1:start+start1+end]
        # Form word
        if mark.find(" ")!=-1:
            a = mark.split(" ")
            mark = ''.join(a)
        elif mark.find("-")!=-1:
            a = mark.split("-")
            mark = ''.join(a)
        mark = mark.title()
        # Fill dictionary
        dictionary_mark[mark] = code
        start0 = start_mark+start1+end
    dictionary_mark["Other"] = "0"

# Complete dictionary for model
def Fill_Dictionary_Model(data,dictionary_model,brand):
    brand_next = brand[0]
    # Get code
    start0 = data.find('<ul class="facets-multi-select-container model-list">')
    end_final = start0+data[start0:].find('</ul>')
    k=0
    m=0
    stop = False
    last = False
    while True:
        start = start0
        str1 = '<input autocomplete="off" type="checkbox" name="model" '
        start1 = data[start:].find(str1) + 8
        # Find which brand the models refer to
        str_ending = '<li class="multi-select-option-group">'
        end1 = data[start0:].find(str_ending)
        if str(end1)=="-1":
            end_final = start0+data[start0:].find('</ul>')
            b = brand_next
            last = True
        else:
            end_final = start0+end1
            end2 = data[start0+end1:].find('<span>')+6
            end3 = data[start0+end1:].find('</span>')
            brand_next = data[start0+end1+end2:start0+end1+end3]
            if (brand_next in brand) and stop:
                stop = not(stop)
                b = brand.index(brand_next)         
        end = data[start+start1+len(str1):].find('"')
        code = data[start+start1+len(str1):start+start1+len(str1)+end]
        # Get mark
        start_mark = start+start1+len(str1)+end
        start = start_mark
        str1 = '<span class="multi-select-option-name">'
        start1 = data[start:].find(str1) + len(str1)
        end = data[start+start1:].find('</span>')
        mark = data[start+start1:start+start1+end]
        # Form word
        if mark.find(" ")!=-1:
            a = mark.split(" ")
            mark = ''.join(a)
        elif mark.find("-")!=-1:
            a = mark.split("-")
            mark = ''.join(a)
        mark = mark.title()
        # Fill dictionary
        start0 = start_mark+start1+end
        if k>=2:
            if int(start0) >= int(end_final):
                if (stop and last) or m>=len(brand):
                    break
                else:
                    m+=1
                    stop = not(stop)
        if len(mark)<=10:
            keys=(mark,brand[m])
            dictionary_model[keys] = code      
            k+=1

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
            return " "
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
        try:
            if cont[0].upper()=="Y":    
                continue    
            elif cont[0].upper()=="N":    
                break     
            else:
                print " yes or no "
                f.pop()
                fa.pop()
                time.sleep(2)
        except:
            print " You have to give something"
            f.pop()
            fa.pop()
            time.sleep(2)         
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
        try:
            if cont[0].upper()=="Y":    
                continue    
            elif cont[0].upper()=="N":    
                break     
            else:
                print " yes or no "
                f.pop()
                fa.pop()
                time.sleep(2)
        except:
            print " You have to give something"
            f.pop()
            fa.pop()
            time.sleep(2)  
    return f       

# Get Brand Filters from user
def Get_Brand(dictionary_mark):
    f = []
    fa = []
    brand_out = []
    while True:
        if len(f)==len(dictionary_mark):
            print "\n- All filters are selected -"
            break        
        clear()
        print "You have "+str(len(f))+" filters"   
        print " Other - if you aren't sure what brand you want"
        if len(f)==0:    
            print "  1 - no filter\n"  
        else:    
            print "  1 - finished with the filters\n"
        while True:        
            i = raw_input(" Give car's brand :\n")    
            if i==" ":    
                print " You have to give something"    
            else:    
                break  
        if i.find(" ")!=-1:
            a = i.split(" ")
            i = ''.join(a)
        if i.find("-")!=-1:
            a = i.split("-")
            i = ''.join(a)
        i = i.title()
        if i in fa:        
            print " Give car's brand only once"    
            time.sleep(2)    
            continue    
        if i=="1":    
            break    
        try:    
            f.append("&make="+dictionary_mark[i])    
            fa.append(i)  
            brand_out.append(i)
        except:    
            print " This brand doesn't exist in our system"    
            time.sleep(2)    
            continue     
        while True:    
            cont = raw_input(" Add more brands ? ( yes / no )\n")    
            if cont==" ":    
                print " You have to give something"    
            else:    
                break    
        try:
            if cont[0].upper()=="Y":    
                continue    
            elif cont[0].upper()=="N":    
                break     
            else:
                print " yes or no "
                f.pop()
                fa.pop()
                brand_out.pop()
                time.sleep(2)
        except:
            print " You have to give something"
            f.pop()
            fa.pop()
            brand_out.pop()
            time.sleep(2)       
    return [f,brand_out]

# Get Model Filters from user
def Get_Model(dictionary_model,brands):
    f = []
    for j in brands:
        fa = []
        while True:
            if len(f)==len(dictionary_model):
                print "\n- All filters are selected -"
                break        
            clear()
            print "You have "+str(len(f))+" filters"
            if len(f)==0:    
                print "  1 - no filter\n"  
            else:    
                print "  1 - finished with the filters\n"
            while True:        
                i = raw_input(" Give "+j+"'s model :\n")    
                if i==" ":    
                    print " You have to give something"    
                else:    
                    break  
            if i.find(" ")!=-1:
                a = i.split(" ")
                i = ''.join(a)
            if i.find("-")!=-1:
                a = i.split("-")
                i = ''.join(a)
            i = i.title()
            if i in fa:        
                print " Give car's model only once"    
                time.sleep(2)    
                continue    
            if i=="1":    
                break    
            try:    
                f.append("&model="+dictionary_model[(i,j)])    
                fa.append(i)    
            except:    
                print " This model doesn't exist in our system"    
                time.sleep(2)    
                continue     
            while True:    
                cont = raw_input(" Add more models ? ( yes / no )\n")    
                if cont==" ":    
                    print " You have to give something"    
                else:    
                    break    
            try:
                if cont[0].upper()=="Y":    
                    continue    
                elif cont[0].upper()=="N":    
                    break     
                else:
                    print " yes or no "
                    f.pop()
                    fa.pop()
                    time.sleep(2)
            except:
                print " You have to give something"
                f.pop()
                fa.pop()
                time.sleep(2)
    return f

