import requests
import json
import os
import time
import Input
clear = lambda: os.system('cls')

# Login
payload = {"username":"schinasdionisis@gmail.com","password":"fo04111999"}
session_requests = requests.session()
login_url = "https://www.car.gr/login/"
result = session_requests.post(login_url , data = payload , headers = dict(ReferenceError=login_url))

# Getting info with Input module
site = session_requests.get("https://www.car.gr/classifieds/cars/?sort=dm")
data = site.content
dictionary_mark = {}
Input.Fill_Dictionary(data,dictionary_mark)
f = Input.Get_Mark(dictionary_mark)
filter_brand = ''.join(f)
    # Requesting data with brand filter only
if filter_brand!="":
    list = ["https://www.car.gr/classifieds/cars/?sort=dm",filter_brand]
    url = ''.join(list)
    site = session_requests.get(url)
    data = site.content
    dictionary_model={}
    Input.Fill_Dictionary_Model(data,dictionary_model)
    print dictionary_model
    f = Input.Get_Model(dictionary_model)
    filter_model = ''.join(f)
price_min = Input.Get_Price_Min()
price_max = Input.Get_Price_Max(price_min)
date_start = Input.Get_Starting_Year()
date_end = Input.Get_Ending_Year(date_start)
f = Input.Get_Market_Filters()
filter_market = ''.join(f)
f = Input.Get_Category()
filter_cat = ''.join(f)

# Get results
def Get_Results(page):
    list = ["https://www.car.gr/classifieds/cars/?sort=dm",filter_cat,filter_market,filter_brand,filter_model,"&pg=",str(page),"&price=%3E",str(price_min),"&price-to=%3C",str(price_max),"&registration=%3E",date_start,"&registration=%3C",date_end]
    url = ''.join(list)
    site = session_requests.get(url)
    data = site.content
    return data

data = Get_Results(1)


# Find number of vehicles
start1 = data[0:].find('<li class="disabled"><a><strong>')
start2 = data[start1:].find('g>')+1
end = data[start1:].find('</strong></a></li>')
n = data[start1+start2+1:start1+end]
space = n.find(" ")
numb_veh = int(n[:space])
clear()
print "Vehicles available under your crateria : "+str(numb_veh)


# Find Price / Brand / Model / Year
def Get_Data(a):
    start1 = data[0:].find('<span itemprop="%s"'%a)
    start2 = data[start1:].find('>')
    end = data[start1:].find('</span>')
    word = data[start1+start2+1:start1+end]
    start3 = word.find(';')
    b = word[start3+1:]
    return b

vehicles = []
numb_of_pages = numb_veh/15+1
for i in range(numb_of_pages):
    k = 0
    if i!=0:
        # Get results for more pages
        data = Get_Results(i+1)
    if numb_of_pages==1:
        loop_j = numb_veh
    elif numb_of_pages>1:
        loop_j = 15
    for j in range(loop_j):
        k+=1
        start1 = data[0:].find('<span itemprop="price"')
        start2 = data[start1:].find('>')
        end = data[start1:].find('</span>')
        word = data[start1+start2+1:start1+end]
        start3 = word.find(';')
        cost = word[start3+1:]+" euro"
        if cost=='\xce\xa1\xcf\x89\xcf\x84\xce\xae\xcf\x83\xcf\x84\xce\xb5 \xcf\x84\xce\xb9\xce\xbc\xce\xae'+' euro':
            cost = "Ask for price"
        brand = Get_Data("brand")
        model = Get_Data("model")
        release_date = Get_Data("releaseDate")
        data = data[start1+end:]
        vehicles.append([cost,brand,model,release_date])
    numb_veh -= k
    numb_of_pages -= 1


# Print results
clear()
print "Vehicles available under your crateria : "+str(len(vehicles))
for i in range(len(vehicles)):
    print vehicles[i]