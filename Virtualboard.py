import os
import random
from PIL import Image
from AbstractBoard import AbstractBoard

class Virtualboard(AbstractBoard):
  def __init__(self):
    super(self.__class__, self).__init__()

    self.image = Image.open("images/ProjektiveEbene.png")

    # Led Coords
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
      self.c.append((i[0]-1, 900-i[1]+1, i[0]+70.866+1, 900-i[1]-70.866-1))


  def setLeds(self, colors):
    
    #for j in range(len(colors)):
    #  self.w.create_oval(self.c[j][0], self.c[j][1], self.c[j][2], self.c[j][3], fill=colors[j], width=0)
    self.image.show()

