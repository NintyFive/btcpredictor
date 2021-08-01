import smtplib
import os

from datetime import datetime

class Reporter:

	FROM, TO = 'gzhaozhao0@gmail.com', 'guoliang_zhao@outlook.com'
	PASSWORD = '95meimei7758521'
	#progress = True
	text = ""

	def send_msg(subj, msg):
		#subject = subj + str(datetime.utcnow())
		#content = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\n{}"
		#content = content.format(Reporter.FROM, Reporter.TO, subject, msg)
		#mail = smtplib.SMTP('smtp.gmail.com', 587)
		#mail.ehlo()
		#mail.starttls()
		#mail.ehlo()
		#mail.login(Reporter.FROM, Reporter.PASSWORD)
		#mail.sendmail(Reporter.FROM, Reporter.TO, content) 
		#mail.quit()
		#Reporter.text = ""

		subject = subj + str(datetime.utcnow())
		content = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\n{}"
		content = content.format(Reporter.FROM, Reporter.TO, subject, msg)
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		mail.ehlo()
		mail.login(Reporter.FROM, Reporter.PASSWORD)
		mail.sendmail(Reporter.FROM, Reporter.TO, content)
		mail.quit()
		Reporter.text = ""

	@staticmethod
	def append(msg):
		Reporter.text += "\n{}".format(msg)

	@staticmethod
	def send_urgent(api_name, etype, err):
		Reporter.send_msg("ALERT: ", "{} ran into an error {} data:\n\n{}".format(api_name, etype, err))

	@staticmethod
	def send_report():
		Reporter.send_msg("Report: ", Reporter.text)

	@staticmethod
	def price_change_alert(msg):
		Reporter.send_msg("Price change: ", msg)
