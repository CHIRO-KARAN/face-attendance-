import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


gmail_user = "ajithkumar.m980@gmail.com"
gmail_pwd = "ramuajith"
FROM = 'ajithkumar.m980@gmail.com'
TO = ['ajithkumar.m980@gmail.com'] #must be a list

               
time.sleep(1)
msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] =("Unauthorized person")
time.sleep(1)
fp = open("1.txt", 'rb')
time.sleep(1)
img = MIMEText(fp.read())
time.sleep(1)
fp.close()
time.sleep(1)
msg.attach(img)
time.sleep(1)
try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        print( "smtp.gmail")
        server.ehlo()
        print ("ehlo")
        server.starttls()
        print ("starttls")
        server.login(gmail_user, gmail_pwd)
        print ("reading mail & password")
        server.sendmail(FROM, TO, msg.as_string())
        print ("from")
        server.close()
        print ('successfully sent the mail')
except:
        print ("failed to send mail")
