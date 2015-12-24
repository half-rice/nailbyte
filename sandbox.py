import requests
from bs4 import BeautifulSoup

url = "https://api.github.com/events"

request = requests.get(url)
data = request.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
  print(link.get('href'))