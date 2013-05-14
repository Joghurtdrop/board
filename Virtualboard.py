import os
from Tkinter import *
import random
from PIL import ImageTk
from AbstractBoard import AbstractBoard

class Virtualboard(AbstractBoard):
  def __init__(self):
    self.master = Tk()
    self.w = Canvas(self.master, width=900, height=900)

    self.image = ImageTk.PhotoImage(file = "images/ProjektiveEbene.png")
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
    c = list()
    c.append((815.146, 319.083))
    c.append((680.231, 644.798))
    c.append((354.516, 779.713))
    c.append(( 28.802, 644.798))
    c.append((202.182, 471.417))
    c.append((354.516, 496.249))
    c.append((506.850, 471.417))
    c.append((531.682, 319.083))
    c.append((354.516, 319.083))
    c.append((177.351, 319.083))
    c.append((202.182, 166.749))
    c.append((354.516, 141.918))
    c.append((506.850, 166.749))

    self.c = list()
    for i in c:
      self.c.append((i[0], 900-i[1], i[0]+70.866, 900-i[1]-70.866))

  def drawCircles(self, cols):
    self.w.create_image(0, 0, image = self.image, anchor = NW )
    
    #for j in range(len(self.c)):
    #  self.w.create_oval(self.c[j][0], self.c[j][1], self.c[j][2], self.c[j][3], fill="#000", width=0)
    
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
