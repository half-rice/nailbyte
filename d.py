import string
import random
import sys
import os
from tkinter import *
from tkinter import filedialog
from pic import *

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.grid(sticky='WNES')
    for x in range(4):
      frame.columnconfigure(x, weight=1)
    frame.rowconfigure(6, weight=1)
    # frame.pack()

    self.pics = []

    self.chars = string.ascii_letters + string.digits
    self.startingCount = IntVar()
    self.count = 0

    self.path = StringVar()
    self.target = StringVar()
    self.name = StringVar()
    self.length = StringVar()
    self.spacer = StringVar()
    self.digits = StringVar()
    self.string = StringVar()
    self.status = StringVar()

    # phantom row
    # self.label1 = Label(frame, width=20, text="label1")
    # self.label1.grid(row=0, column=0)
    # self.label1.columnconfigure(0, weight=1)
    # self.label2 = Label(frame, width=20, text="label2")
    # self.label2.grid(row=0, column=1)
    # self.label2.columnconfigure(0, weight=1)
    # self.label3 = Label(frame, width=20, text="label3")
    # self.label3.grid(row=0, column=2)
    # self.label3.columnconfigure(0, weight=1)
    # self.label4 = Label(frame, width=20, text="label4")
    # self.label4.grid(row=0, column=3)
    # self.label4.columnconfigure(0, weight=1)

    # row 1 - Path
    self.pathLabel = Label(frame, text="Current Directory")
    self.pathLabel.grid(row=0, column=0, sticky='E')
    self.pathLabel.columnconfigure(0, weight=1)

    self.pathEntry = Entry(frame)
    self.pathEntry.grid(row=0, column=1, columnspan=2, sticky='WE')
    self.pathEntry.columnconfigure(0, weight=2)

    self.path.set(os.getcwd())
    self.pathEntry["textvariable"] = self.path

    self.pathButton = Button(frame, text="...", command=self.askPath)
    self.pathButton.grid(row=0, column=3, sticky='W')
    self.pathButton.columnconfigure(0, weight=1)

    # self.diag = Button(frame, text="Q", command=self.diag)
    # self.diag.grid(row=0, column=3, sticky='W')
    # self.diag.columnconfigure(0, weight=1)

    # row 2 - Target
    self.targetLabel = Label(frame, text="Target Directory")
    self.targetLabel.grid(row=1, column=0, sticky='E')

    self.targetEntry = Entry(frame)
    self.targetEntry.grid(row=1, column=1, columnspan=2, sticky='WE')

    self.target.set(self.path.get())
    self.targetEntry["textvariable"] = self.target

    self.targetButton = Button(frame, text="...", command=self.askTarget)
    self.targetButton.grid(row=1, column=3, sticky='W')


    # row 3 - Name
    self.nameLabel = Label(frame, text="Name")
    self.nameLabel.grid(row=2, column=0, sticky='E')

    self.nameEntry = Entry(frame)
    self.nameEntry.grid(row=2, column=1, sticky='WE')

    self.name.set("")
    self.nameEntry["textvariable"] = self.name

    self.testButton = Button(frame, text="Test", command=self.test)
    self.testButton.grid(row=2, column=2, sticky='W')

    # self.nameButton = Button(frame, text="r()", command=self.randomName)
    # self.nameButton.grid(row=1, column=2, sticky='W')


    # row 3 - Name Length
    # self.lengthLabel = Label(frame, text="String Length")
    # self.lengthLabel.grid(row=2, column=0, sticky='E')

    # self.length.set("5")
    # self.lengthSpinbox = Spinbox(frame, width=2, from_=0, to=10, 
    #   increment=1, textvariable=self.length)
    # self.lengthSpinbox.grid(row=2, column=1, sticky='W')


    # row 4 - Spacer
    # self.spacerLabel = Label(frame, text="Spacer")
    # self.spacerLabel.grid(row=3, column=0, sticky='E')

    # self.spacerEntry = Entry(frame, width=4)
    # self.spacerEntry.grid(row=3, column=1, sticky='W')

    # self.spacer.set("")
    # self.spacerEntry["textvariable"] = self.spacer 


    # row 5 - Digits
    self.digitsLabel = Label(frame, text="+ Digits")
    self.digitsLabel.grid(row=4, column=0, sticky='E')

    self.digits.set("4")
    self.digitsSpinbox = Spinbox(frame, width=2, from_=0, to=10,
      increment=1, textvariable=self.digits)
    self.digitsSpinbox.grid(row=4, column=1, sticky='W')

    # Count
    self.startingCountLabel = Label(frame, text="Start At #")
    self.startingCountLabel.grid(row=5, column=0, sticky='E')

    self.startingCountEntry = Entry(frame, width=4)
    self.startingCountEntry.grid(row=5, column=1, sticky='W')

    self.startingCount.set(1)
    self.startingCountEntry["textvariable"] = self.startingCount


    # row 6 - String
    # self.stringLabel = Label(frame, text="String")
    # self.stringLabel.grid(row=5, column=0, sticky='E')

    # self.stringEntry = Entry(frame)
    # self.stringEntry.grid(row=5, column=1, sticky='W')

    # self.string.set("")
    # self.stringEntry["textvariable"] = self.string

    # self.stringButton = Button(frame, text="str", command=self.getString)
    # self.stringButton.grid(row=5, column=2, sticky='W')


    # row 7 - Listboxes
    self.oldNameListbox = Listbox(frame, width=40, height=20, bd=1)
    self.oldNameListbox.grid(row=6, column=0, columnspan=2, sticky='WNES')

    self.newNameListbox = Listbox(frame, width=40, height=20, bd=1)
    self.newNameListbox.grid(row=6, column=2, columnspan=2, sticky='WNES')

    # row 8 - Run
    # self.testButton = Button(frame, text="Test", command=self.test)
    # self.testButton.grid(row=5, columnspan=4, sticky='WNES')

    # status bar
    self.statusBar = Label(frame, text="nothing to report", bd=1, relief=SUNKEN, anchor=W)
    self.statusBar.grid(row=7, column=0, columnspan=4, sticky='WNES')

    self.status.set("Status: ok")
    self.statusBar["textvariable"] = self.status


  def askPath(self):
    path_old = self.path.get()
    path = filedialog.askdirectory()

    if path != path_old and len(path) > 0:
      self.path.set(path)
    else:
      self.path.set(path_old)

  def askTarget(self):
    target_old = self.target.get()
    target = filedialog.askdirectory()

    print(target_old)

    if target != target_old and len(target) > 0:
      self.target.set(target)
    else:
      self.target.set(target_old)

  def getString(self):
    s = ""
    s += self.getNameString()
    s += self.getSpacerString()
    s += self.getDigitsString()
    self.string.set(s)
    return self.string.get()

  def getNameString(self):
    return self.name.get()

  def randomName(self):
    string = ''.join(random.SystemRandom().choice(self.chars) for _ in range(int(self.length.get())))
    self.name.set(string)

  def getSpacerString(self):
    return self.spacer.get()

  def getDigitsString(self):
    return self.padZeros()

  def padZeros(self):
    zeros = ""
    digits = int(self.digits.get()) 
    count = self.startingCount.get() + self.count
    while len(str(count)) < digits:
      zeros += "0"
      digits -= 1
    # print(zeros + str(count))
    return (zeros + str(count))

  def test(self):
    self.oldNameListbox.delete(0, END)
    self.newNameListbox.delete(0, END)
    self.pics.clear()
    self.count = 0
    for file in os.listdir(self.path.get()):
      if self.isPic(file):
        pic = Pic(file)

        # config pic
        pic.path = os.path.join(self.path.get(), pic.name, pic.ext)

        # pic.path = self.path.get() + "/" + pic.name + pic.ext
        pic.location = self.path.get()
        pic.setTarget(name=self.getString(),location=self.target.get())
        # pic.targetName = self.getString()
        self.addPic(pic)
        self.oldNameListbox.insert(END, (str(self.count) + ": " + pic.path))
        self.newNameListbox.insert(END, (str(self.count) + ": " + pic.targetPath))
        # self.oldNameListbox.insert(END, (str(self.count) + ": " + pic.location 
        #   + "/" + pic.name + pic.ext))
        # self.newNameListbox.insert(END, (str(self.count) + ": " + pic.targetLocation 
        #   + "/" + pic.targetName + pic.ext))
        self.count += 1
    self.status.set("Pics: " + str(len(self.pics)))
    # for i in range(len(self.pics)):
    #   self.pics[i].printAll()

  def isPic(self, file):
    picExtensions = ('.jpg', '.jpeg', '.png', '.gif', '.tif', '.bmp')
    if file.lower().endswith(picExtensions):
      return True
    return False

  def addPic(self, file):
    self.pics.append(file)

  def diag(self):
    print("path: " + self.path.get())
    print("string: " + self.string.get())
    print("length: " + self.length.get())
    print("digits: " + self.digits.get())




root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
app = App(root)
root.mainloop()