from bs4 import BeautifulSoup
import requests
import json

# Login
payload = {"username":"schinasdionisis@gmail.com","password":"fo04111999"}
session_requests = requests.session()
login_url = "https://www.car.gr/login/"
result = session_requests.post(login_url , data = payload , headers = dict(ReferenceError=login_url))

# Get results
price = int(raw_input("Give max price for car : \n"))
url = "https://www.car.gr/classifieds/cars/?fs=1&condition=%CE%9C%CE%B5%CF%84%CE%B1%CF%87%CE%B5%CE%B9%CF%81%CE%B9%CF%83%CE%BC%CE%AD%CE%BD%CE%BF&offer_type=sale&category=18&make=22&make=22&price-to=%3"+"C%i" %price
site = session_requests.get(url)
data = site.content

# Find number of vehicles
start1 = data[0:].find('<li class="disabled"><a><strong>')
start2 = data[start1:].find('g>')+1
end = data[start1:].find('</strong></a></li>')
n = data[start1+start2+1:start1+end]
space = n.find(" ")
numb = int(n[:space])
print "Vehicles available in your crateria : "+str(numb)

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
for i in range(numb):
    start1 = data[0:].find('<span itemprop="price"')
    start2 = data[start1:].find('>')
    end = data[start1:].find('</span>')
    word = data[start1+start2+1:start1+end]
    start3 = word.find(';')
    cost = word[start3+1:]+" euro"
    if cost=='\xce\xa1\xcf\x89\xcf\x84\xce\xae\xcf\x83\xcf\x84\xce\xb5 \xcf\x84\xce\xb9\xce\xbc\xce\xae'+' euro':
        cost = "Ask for price"
    start1 = data[0:].find('<span itemprop="brand">')
    start2 = data[start1:].find('>')
    end = data[start1:].find('</span>')
    word = data[start1+start2+1:start1+end]
    start3 = word.find(';')
    brand = word[start3+1:]

    data = data[start1+end:]
    vehicles.append([cost,brand])

for i in range(numb):
    print vehicles[i]