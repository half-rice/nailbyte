import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import requests
from bs4 import BeautifulSoup

# url = "https://google.com"

# r = requests.get(url)
# data = r.text
# soup = BeautifulSoup(data, "html.parser")

# for link in soup.find_all('a'):
#   print(link.get('href'))

class Test(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setGeometry(300,300,300,220)
    self.setWindowTitle('NailByte')
    self.setWindowIcon(QIcon('web.png'))
    self.show()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  test = Test()
  sys.exit(app.exec_())
