from bs4 import BeautifulSoup
import requests
from os import system

system("cls")
url = "https://www.aljazeera.com/news/2022/5/26/ukraine-pleads-for-heavy-weapons-to-counter-russian-offensive-liveblog"
website = requests.get(url)
soup = BeautifulSoup(website.text, 'html.parser')
arr = soup.find_all('h2')
for i in arr[4:]:
    print("          -------------------------------------------------------------------------------------------------------------")
    print("          " + str(i.text))
print("          -------------------------------------------------------------------------------------------------------------")