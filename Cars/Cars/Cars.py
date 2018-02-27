import requests
import json

# Login
payload = {"username":"schinasdionisis@gmail.com","password":"fo04111999"}
session_requests = requests.session()
login_url = "https://www.car.gr/login/"
result = session_requests.post(login_url , data = payload , headers = dict(ReferenceError=login_url))

# Get results
def Get_Results(page,price):
    list = ["https://www.car.gr/classifieds/cars/?category=18&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&make=22&make=22&offer_type=sale&pg=",str(page),"&price-to=%3C",str(price)]
    url = ''.join(list)
    site = session_requests.get(url)
    data = site.content
    return data
    
price = int(raw_input("Give max price for car : \n"))
data = Get_Results(1,price)

# Find number of vehicles
start1 = data[0:].find('<li class="disabled"><a><strong>')
start2 = data[start1:].find('g>')+1
end = data[start1:].find('</strong></a></li>')
n = data[start1+start2+1:start1+end]
space = n.find(" ")
numb_veh = int(n[:space])
print "Vehicles available in your crateria : "+str(numb_veh)

# Find prices
def Get_Data(a):
    start1 = data[0:].find('<span itemprop="%s">'%a)
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
        data = Get_Results(i+1,price)
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