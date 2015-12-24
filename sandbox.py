import requests
from bs4 import BeautifulSoup

url = "https://google.com"

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
  print(link.get('href'))