from Tkinter import *
import random
from AbstractBoard import AbstractBoard

class Virtualboard(AbstractBoard):
  def __init__(self):
    self.master = Tk()
    self.w = Canvas(self.master, width=400, height=400)
    self.w.pack()

    self.i = 0

    self.circlesCoords()  

  def toColor(self, color):
    s = '#'
    c = '0123456789abcdef'
  
    for i in color:
      s += c[i / 16]

    return s

  def circlesCoords(self):
    self.c = list()
    for i in range(5):
      self.c.append((50*(i+1),       50,     50*(i+2),          100))
    for i in range(5):
      self.c.append((     300, 50*(i+1),          350,     50*(i+2)))
    for i in range(5):
      self.c.append((300-50*i,      300, 300-50*(i-1),          350))
    for i in range(5):
      self.c.append((      50, 300-50*i,          100, 300-50*(i-1)))

  def drawCircles(self, cols):
    self.w.create_rectangle(  0,   0, 400, 400, fill="white", width=0)
    self.w.create_rectangle(100, 100, 300, 300, fill="blue", width=0)
    
    for i in range(min(len(self.c), len(cols))):
      j = (i+self.i) % len(self.c)
      self.w.create_oval(self.c[j][0], self.c[j][1], self.c[j][2], self.c[j][3], fill=self.toColor(cols[i]), width=0)

  def refresh(self):
    self.drawCircles(self.getGetterClass().get())

  def update(self):
    self.i += 1

    self.refresh()

    self.master.after(1000, self.update)

  def run(self):
    self.update()
    self.master.mainloop()
