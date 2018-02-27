import requests
import json

# Login
payload = {"username":"schinasdionisis@gmail.com","password":"fo04111999"}
session_requests = requests.session()
login_url = "https://www.car.gr/login/"
result = session_requests.post(login_url , data = payload , headers = dict(ReferenceError=login_url))

# Get info from user
pricing = int(raw_input("Give max price for car : \n"))
filters = {1:"&condition=%CE%9A%CE%B1%CE%B9%CE%BD%CE%BF%CF%8D%CF%81%CE%B9%CE%BF",
           2:"&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF",
           3:"&offer_type=sale",
           4:"&offer_type=wanted",
           5:"&offer_type=rent"}
go = True
filter=""
while True:
    if go == True:
        print "Give filters :"
        print " 1 - kainourgio"
        print " 2 - metaxeirismeno"
        print " 3 - pwleitai"
        print " 4 - zhteitai"
        print " 5 - enoikiazetai"
        if filter=="":
            print " 6 - no filter"
        f = raw_input()
        if f=="6":
            break
        try:
            filter = filter+filters[int(f)]
        except:
            print "Input must be : 1 or 2 or 3 or 4 or 5"
            continue
    cont = raw_input("Add more filters ? ( yes / no )\n")
    if cont[0]=="Y" or cont[0]=="y":
        continue
    elif cont[0]=="N" or cont[0]=="n":
        break
    else:
        print " yes or no"
        go == False

# Get results
def Get_Results(page):
    list = ["https://www.car.gr/classifieds/cars/?category=18",filter,"&pg=",str(page),"&price-to=%3C",str(pricing)]
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
print "Vehicles available under your crateria : "+str(numb_veh)

# Find prices
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
for i in range(len(vehicles)):
    print vehicles[i]