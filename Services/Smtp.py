__author__ = 'Dmdv'

import smtplib

setupServer = 'mail.avp.ru'
fromaddr = 'test@yandex.ru'
toaddrs = 'test@yandex.ru'

msg = ("From: %s\r\nTo: %s\r\n\r\n" % (fromaddr, toaddrs))

server = smtplib.SMTP(setupServer)
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, "This is a test message")
server.quit()
