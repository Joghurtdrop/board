import imaplib 
import config

#ssl = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
#ssl.load_cert_chain('faveve.ca.crt')
print(config.imapacc)
mail = imaplib.IMAP4_SSL(host='imap.faveve.uni-stuttgart.de',port=993,keyfile='mykey.pem',certfile='faveve.ca.crt')
r,d = mail.login(config.imapacc,config.imappass) 

#mail.list()
#mail.select("Inbox")

result, data=mail.search(None,'(UNSEEN)')

#latest_email_uid = data[0].split()

print(len(latest_email_uid))
