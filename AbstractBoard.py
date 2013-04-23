
class AbstractBoard:
  def __init__(self):
    self.getterClass = None

  def setGetterClass(self, getterClass):
    self.getterClass = getterClass

  def getGetterClass(self):
    if self.getterClass == None:
      raise Exception('GetterClass nicht angegeben')

    return self.getterClass



