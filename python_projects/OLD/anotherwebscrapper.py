from bs4 import BeautifulSoup
import requests

url = "http://www.youtube.com"
website = requests.get(url)
soup = BeautifulSoup(website.text, 'html.parser')
soup.prettify()
titles = soup.find_all("yt-formatted-string", { "id" : "video-title" })
print(titles)