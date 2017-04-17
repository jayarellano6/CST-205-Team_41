import smtplib 
 #parameters of the email server
 
 
 #security function that connects to the gmail server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
 
msg = "YOUR MESSAGE!"
server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
server.quit()
