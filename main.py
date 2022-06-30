import smtplib as s

obj = s.SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()
obj.login('197r1a0527@gmail.com','Madhuketanpalakurthy@123')
subject = "test Automator"
body = "Greetings from Madhuketan"
message = "subject:{}\n\n{}".format(subject,body)
l = ['madhuketan.13@gmail.com']
obj.sendmail('madhuketan.13@gmail.com',l,message)
print("Mail sent")
obj.quit()



