
from datetime import datetime

class Colorado:
  def __init__(self):
    self.getterClass = None

  def setGetterClass(self, getterClass):
    self.getterClass = getterClass

  def getGetterClass(self):
    if self.getterClass == None:
      raise Exception('GetterClass nicht angegeben')
    
    return self.getterClass

  def get(self):
    getter = self.getGetterClass()
    l = getter.get()

    now = datetime.now()
    r = list()
    for i in l:
      c = [0,0,0]

      # Wenn schon lange her
      if 'date' not in i or i['date'] == None:
        c[0] = 255
      else:
        td = now - i['date']
        hours = td.days*24 + td.seconds / 3600
        if hours > 24*3:
          c[0] = 255

      
      # Wenn Uni-intern
      if 'from' in i and i['from'].find('uni-stuttgart.de') != -1:
        c[2] = 255

      if c[0] == 0 and c[1] == 0 and c[2] == 0:
        c[1] = 255
      r.append(c)

    return r

