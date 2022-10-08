import tkinter
from bs4 import BeautifulSoup
import requests
import datetime
from tkinter import *

class Weather:
    def __init__(self):
        self.degree = None
        self.day = None
        self.hour = None
        self.month = None
        self.humidity = None
    
    def get_data(self):
        url = "https://weather.com/weather/tenday/l/Oradea+Bihor+Romania?canonicalCityId=55523e92d7380c12893a4bdf44f10b668ea8000df7682275bc46c3218fa78f47"
        website = requests.get(url)
        soup = BeautifulSoup(website.text, 'html.parser')
        soup.prettify()
        temps = soup.find_all("span", { "data-testid":"TemperatureValue" })
        humidity = soup.find_all("span", { "data-testid":"PercentageValue" })
        self.humidity = humidity[1].text
        self.degree = str(int(temps[1].text[:-1])-32)+"C°"
        self.hour = datetime.datetime.now().hour
        self.day = datetime.datetime.now().day
        self.month = datetime.datetime.now().month
    
    def __str__(self):
        return f"{self.degree} {self.day} {self.hour} {self.month} {self.humidity}"

root = Tk()
degree = StringVar()
humidity = StringVar()
month = StringVar()
day = StringVar()
hour = StringVar()
mai = Frame(root, bg="black")
mai.pack()
f1 = Frame(mai, bg="black")
f1.pack()
t1 = Label(f1, textvariable=degree, fg="red", bg="black", font=("Arial", 30))
t1.pack(side="left")
t2 = Label(f1, textvariable=humidity, fg="red", font=("Arial", 30), bg="black")
t2.pack(side="right")
f2 = Frame(mai, bg="black")
f2.pack()
t3 = Label(f2, textvariable=month, fg="red", font=("Arial", 30), bg="black")
s1 = Label(f2, text="/", fg="red", font=("Arial", 30), bg="black")
t4 = Label(f2, textvariable=day, fg="red", font=("Arial", 30), bg="black")
s2 = Label(f2, text="/", fg="red", font=("Arial", 30), bg="black")
t5 = Label(f2, textvariable=hour, fg="red", font=("Arial", 30), bg="black")
t3.pack(side="left")
s1.pack(side="left")
t4.pack(side="left")
s2.pack(side="left")
t5.pack(side="left")
    
def update(dat=Weather()):
    print(1)
    dat.get_data()
    print(2)
    degree.set(dat.degree)
    print(3)
    humidity.set(dat.humidity)
    print(4)
    month.set(dat.month)
    print(5)
    day.set(dat.day)
    print(6)
    hour.set(dat.hour)
    print(7)
    root.after(5, update)
    return ""

update()
mainloop()