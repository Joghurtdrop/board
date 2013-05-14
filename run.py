import os
import imap
import config
import colorado
import Virtualboard


if os.path.dirname(__file__):
  os.chdir(os.path.dirname(__file__))


mail = imap.Imap()
mail.setLogin(config.imaphost, config.imapacc,config.imappass, config.imapcertfile)

colors = colorado.Colorado()
colors.setGetterClass(mail)

vibo = Virtualboard.Virtualboard()
vibo.setGetterClass(colors)

vibo.run()

mail.logout()

