
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
      
      # Wenn Uni-intern
      index = 1
      if 'from' in i and i['from'].find('uni-stuttgart.de') != -1:
        index = 2


      # Wenn schon lange her
      if 'date' not in i or i['date'] == None:
        c[0] = 255
      else:
        td = now - i['date']
        minutes = td.days*24*60 + td.seconds / 60
        if minutes < 24*60:
          c[0] = 0
          c[index] = 255
        else:
          t = min(2*255, 2*255*(minutes - 24*60) / (24*60*6))
          c[0] = min(t, 255)
          c[index] = min(2*255-t, 255)

      r.append(c)

    return r

