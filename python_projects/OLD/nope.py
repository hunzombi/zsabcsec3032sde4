from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/Oradea+Bihor+Romania?canonicalCityId=55523e92d7380c12893a4bdf44f10b668ea8000df7682275bc46c3218fa78f47"
website = requests.get(url)
soup = BeautifulSoup(website.text, 'html.parser')
soup.prettify()
titles = soup.find_all("span", { "data-testid":"TemperatureValue" })
farrenheight = titles[1].text[:-1]
celsius = (int(farrenheight)-32)*5/9

print(farrenheight)
print(celsius)