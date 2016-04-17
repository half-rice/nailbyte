import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget
from bs4 import BeautifulSoup

# url = "https://google.com"

# r = requests.get(url)
# data = r.text
# soup = BeautifulSoup(data, "html.parser")

# for link in soup.find_all('a'):
#   print(link.get('href'))

if __name__ == "__main__":
  app = QApplication(sys.argv)

  w = QWidget()
  w.resize(250,150)
  w.move(300,300)
  w.setWindowTitle("nailbyte")
  w.show()

  sys.exit(app.exec_())
