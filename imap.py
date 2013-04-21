import imaplib 
import config
import subprocess

subprocess.call('openssl genrsa -out mykey.pem 1034 &> /dev/null', shell=True)


mail = imaplib.IMAP4_SSL(host='imap.faveve.uni-stuttgart.de',port=993,keyfile='mykey.pem',certfile='faveve.ca.crt')
r,d = mail.login(config.imapacc,config.imappass) 

mail.list()
mail.select("Inbox")


result, data=mail.search(None,'(UNSEEN)')

latest_email_uid = data[0].split()

print(len(latest_email_uid))

subprocess.call('rm -f mykey.pem',shell=True)
