
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
    cols = self.getGetterClass().get()

    colors = range(self.leds)
    for i in range(self.leds): #len(self.c), len(cols))):
      j = (self.i-i) % len(self.c)
      if i < len(cols):
        colors[j] = self.toColor(cols[i])
      else:
        colors[j] = "#000"

    self.setLeds(colors)

  def update(self):
    self.i += 1

    self.refresh()

  # Run muss alle x Sekunden die update-funktion aufrufen
  def run(self):
    pass
