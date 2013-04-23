import imaplib 
import subprocess
import datetime

"""
" Klasse, mit der ein Imapserver abgefragt werden kann
"""
class Imap:

  def setLogin(self, host, user, password, certfile):
    self.login = (host, user, password, certfile)

  def getLogin(self):
    if self.login == None:
      raise Exception('Keine Logindaten angegeben')

    return self.login

  def __init__(self):
    self.mail = None
    self.login = None

  def logout(self):
    self.getMail().close()
    self.getMail().logout()
    self.mail = None

  def getMail(self):
    if self.mail == None:
      logind = self.getLogin()
      subprocess.call('openssl genrsa -out tmpkey.pem 1034 &> /dev/null', shell=True)
      self.mail = imaplib.IMAP4_SSL(host=logind[0],keyfile='tmpkey.pem',certfile=logind[3])
      r,d = self.mail.login(logind[1], logind[2]) 

    return self.mail

  def getMailInfo(self, id):
    mail = self.getMail()

    try:
      data = mail.fetch(id, "(INTERNALDATE BODY[HEADER.FIELDS (FROM)])")
      sender = data[1][0][1].strip()
      datestr = data[1][0][0].strip()
      datestart = datestr.find('"')
      dateend = datestr.rfind('"')
      date = datetime.datetime.strptime(datestr[datestart+1:dateend-6], '%d-%b-%Y %H:%M:%S') if datestart > -1 and dateend > -1 else None
    finally:
      # Auf ungelesen setzen
      mail.store(id,'-FLAGS','(\Seen)')

    return {'from': sender, 'date': date}
  
 
  """
  " Gibt eine Liste von Datum Absender-Tupeln zurueck
  """  
  def getUnseen(self):
    mail = self.getMail()

    mail.select("Inbox")

    result, data=mail.search(None,'(UNSEEN)')
    if len(data[0]) == 0:
      return list()

    ids = data[0].split(" ")

    data = list()
    for id in ids:
      data.append(self.getMailInfo(id))

    return data

   
