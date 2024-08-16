import smtplib as s

object = s.SMTP("smtp.gmail.com", 587) # 587 is a gmail port number
object.ehlo()
object.starttls()
object.login('abc@gmail.com','1234')
subject = 'test python'
body = "Python Programming"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['1abc@gmail.com',
           '2abc@gmail.com',
           '3abc@gmail.com']
object.sendmail('abc@gmail.com', listadd,message)
print("Send mail")
object.quit()

 
