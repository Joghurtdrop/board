import time

class AbstractBoard(object):
  def __init__(self):
    self.getterClass = None

    self.i = 0
    self.leds = 13

  def setGetterClass(self, getterClass):
    self.getterClass = getterClass

  def getGetterClass(self):
    if self.getterClass == None:
      raise Exception('GetterClass nicht angegeben')

    return self.getterClass

  # Muss implementiert werden, setzt die Leds
  def setLeds(self, colors):
    pass

  def toColor(self, color):
    s = '#'
    c = '0123456789abcdef'
  
    for i in color:
      s += c[i / 16]

    return s

  def refresh(self):
    colors = range(self.leds)
    
    cols = self.getGetterClass().get()
    
    # Effekt, wenn keine Connection vorhanden ist
    if cols == None:
      cols = [(255,0,0) for i in colors] if self.i % 2 == 0 else list()
    elif len(cols) == 0:
      cols = [(255,255,255) for i in colors] if self.i % 2 == 0 else [(0,0,0)]
    
    for i in range(self.leds): #len(self.c), len(cols))):
      j = (self.i-i) % self.leds
      if i < len(cols):
        colors[j] = cols[i]
      else:
        colors[j] = (0,0,0)
   
    print(colors) 
    return
    self.setLeds(colors)

  def update(self):
    self.i = (self.i + 1) % self.leds

    self.refresh()

  # Run muss alle x Sekunden die update-funktion aufrufen
  def run(self):
    while True:
      self.update()
      time.sleep(1)
