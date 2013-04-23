
import imap
import config


mail = imap.Imap()
mail.setLogin(config.imaphost, config.imapacc,config.imappass, config.imapcertfile)
print(mail.getUnseen())
mail.logout()

