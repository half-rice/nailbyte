import sys
import os


class Pic(object):
  def __init__(self, file):
    self.path = ""
    # self.path = os.path.realpath()
    self.name, self.ext = os.path.splitext(file)
    self.location = os.getcwd()
    self.targetPath = ""
    self.targetName = ""
    self.targetLocation = ""

  def buildPath(self):
    return self.location + self.name + self.ext

  def setTarget(self, name, location):
    self.targetName = name
    self.targetLocation = location
    if self.targetLocation[-1] == "/":
      self.targetPath = self.targetLocation + self.targetName + self.ext
    else:
      self.targetPath = self.targetLocation + "/" + self.targetName + self.ext


  def printAll(self):
    print("\n----- pic -----")
    print("path: " + self.path)
    print("name: " + self.name + self.ext)
    # print("loc: " + self.location)
    # print("type: " + self.ext)
    print("targetPath: " + self.targetPath)
    print("targetName: " + self.targetName + self.ext)
    # print("targetLoc: " + self.targetLocation)
    print("----------------\n")