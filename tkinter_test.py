import Tkinter as tk
import os
import requests
import Input
def write_slogan():
    print("Tkinter is easy to use!")
def print1():
	print ("o hi mark")
def b1():
    # Login
    session_requests = requests.session()
    login_url = "https://www.car.gr/login/"
    result = session_requests.post(login_url , headers = dict(ReferenceError=login_url))

    # Getting info with Input module
    site = session_requests.get("https://www.car.gr/classifieds/cars/?sort=dm")
    data = site.content
    dictionary_mark = {}
    Input.Fill_Dictionary(data,dictionary_mark)
    f = Input.Get_Brand(dictionary_mark)
    filter_brand = ''.join(f[0])
        # Requesting data with brand filter only
    if filter_brand!="":
        list = ["https://www.car.gr/classifieds/cars/?sort=dm",filter_brand]
        url = ''.join(list)
        site = session_requests.get(url)
        data = site.content
        dictionary_model={}
        Input.Fill_Dictionary_Model(data,dictionary_model,f[1])
        f = Input.Get_Model(dictionary_model,f[1])
        filter_model = ''.join(f)
    else:
        filter_model =" "
    price_min = Input.Get_Price_Min()
    if price_min!=" ":
        price_max = Input.Get_Price_Max(price_min)
    else:
        price_max = Input.Get_Price_Max(0)
    date_start = Input.Get_Starting_Year()
    date_end = Input.Get_Ending_Year(date_start)
    f = Input.Get_Market_Filters()
    filter_market = ''.join(f)
    f = Input.Get_Category()
    filter_cat = ''.join(f)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Search",
                   command=print1)
slogan.pack(side=tk.LEFT)
button1= tk.Button(frame, text="Config", fg="red",command=b1)
button1.pack(side=tk.TOP)
root.mainloop()

hostname = "www.car.gr"
response = os.system("ping -n 1 " + hostname)

