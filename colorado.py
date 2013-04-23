
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
      c = ['0','0','0']

      # Wenn schon lange her
      if 'date' not in i or i['date'] == None:
        c[0] = 'f'
      else:
        td = now - i['date']
        hours = td.days*24 + td.seconds / 3600
        if hours > 24*3:
          c[0] = 'f'

      
      # Wenn Uni-intern
      if 'from' in i and i['from'].find('uni-stuttgart.de') != -1:
        c[2] = 'f'

      c = c[0]+c[1]+c[2]
      if c == '000':
        c = '0f0'
      r.append(c)

    return r

