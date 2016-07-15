#Quik Mail Script

import smtplib
import string

def main():

    print "======"
    print "MAILER"
    print "======\n\n"
    print "1. my email adress\n2. my email adress\n3. Exit"
    ch = int(raw_input("Select an option : "))
    if ch == 1:
        gmail()
    elif ch == 2:
        hotmail()
    elif ch == 3:
        exit()
    else:
        print "Invalid option"


def gmail():
    print "\n"   
    uid = "mygmail@gmail.com"
    pwd = "mypassword."
    to = raw_input("\nTo : ")
    subject = raw_input("Subject : ")
    content = raw_input("Message : ")
    mail_server = 'smtp.gmail.com'
    message = string.join((
        "From : %s" % uid,
        "To : %s" % to,
        "Subject : %s" % subject,
        "",
        content,
    ), "\r\n")   
    send_mail(uid, pwd, to, message, mail_server)
    
def hotmail():
    print "\n"
    uid = "myhotmail@hotmail.com"
    pwd = "mypassword"
    to = raw_input("\nTo : ")
    subject = raw_input("Subject : ")
    content = raw_input("Message : ")
    mail_server = 'smptp.live.com'
    message = string.join((
        "From : %s" % uid,
        "To : %s" % to,
        "Subject : %s" % subject,
        "",
        content,
    ), "\r\n")
    send_mail(uid, pwd, to, message, mail_server)
    
def send_mail(uid, pwd, to, message, mail_server):
    server = smtplib.SMTP(mail_server, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(uid, pwd)
    server.sendmail(uid, to, message)
    server.close()
    
