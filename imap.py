import imaplib 
import ssl


#ssl = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
#ssl.load_cert_chain('faveve.ca.crt')

mail = imaplib.IMAP4_SSL(host='imap.faveve.uni-stuttgart.de',port=993,keyfile=None,certfile='faveve.ca.crt')
r,d = imap.login('fs-mathe', '$PW')

#mail.list()
#mail.select("Inbox")

#result, data=mail.search(None,'(UNSEEN)')

#latest_email_uid = data[0].split()

#print(len(latest_email_uid))
