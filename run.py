
import imap
import config
import colorado

mail = imap.Imap()
mail.setLogin(config.imaphost, config.imapacc,config.imappass, config.imapcertfile)

colors = colorado.Colorado()
colors.setGetterClass(mail)

print(colors.get())

mail.logout()

