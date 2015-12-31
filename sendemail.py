import smtplib
def sendemail(fromaddr, password):
	toaddrs  = fromaddr
	msg = 'The crawl Finish!!!'
	username = fromaddr
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()