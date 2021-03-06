import smtplib
import os
from email.message import EmailMessage

class Mail:
	
	EMAIL_ADDR = ""
	EMAIL_PWD = ""

	def __init__(self,mail,pwd):
		self.EMAIL_ADDR = mail
		self.EMAIL_PWD = pwd

	def sendMail(self,mail,name,subj,body):
		print(body)
		msg = EmailMessage()
		msg['Subject'] = subj
		msg['From'] = name
		msg['To'] = mail
		msg.set_content(body)
		try:
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.starttls()
				smtp.login(self.EMAIL_ADDR,self.EMAIL_PWD)
				smtp.send_message(msg)
				print("sent mail")
				return 1
		except Exception as e:
			print(e)