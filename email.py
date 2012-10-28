#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bonnie
#
# Created:     31/08/2011
# Copyright:   (c) Bonnie 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
def right_justify(name):
    a =''
    for i in range(0,70):
        a += ' '
    a += name
    print name

def check_fermet(a,b,c,n):
#a^n + b^n = c^n, n must be greater than 2
    if(n<=2):
        print "please retry, n must be greater than 2"
    else:
        if((a**n +b**n)==(c**n)):
            print "he's wrong"
        else:
            print "he's right... this time"

def check_fermetprompt():
    try:
        a=raw_input("what is a")
        b=raw_input("what is b")
        c=a*b
    except:
        print('please enter an integer')

def factorial(n):
    #n(n-1)!
    #if n=0, then return 1
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

def is_palindrome(word):
    if(word==''):
        print 'is palindrome'
    elif(word[0]==word[-1]):
        is_palindrome(word[1:-1])
    else:
        print 'is not palindrome'

def ex111():
    f= open('C:\\Users\\Bonnie\\Desktop\\text.txt')
    a=f.read()
    fileall=a.replace('\n','')
    print type(fileall)
    m=''
    words = dict()

##    i=0
    for a in fileall:
        if(a==" "):
            words[m]=0
            m=''
        else:
            m+=a
    print words

##*0.000000 2682972
##*
##0a[0]
##

def email_notify():
    import os
    import smtplib #library to send and receive e-mail
    import string

    from email import Encoders #the email package
    from email.MIMEBase import MIMEBase
    from email.MIMEMultipart import MIMEMultipart
    from email.Utils import formatdate

    filePath = r'C:\\Users\\Bonnie\\Desktop\\drawingskillz.jpg'

    SUBJECT = "TEST email from Python2"
    TO="leatherface123@gmail.com"
    FROM ="yuqiaoyan@gmail.com"
    text='Did my Python email attachment code work? E-mail me back if you saw it!!'

    msg = MIMEMultipart()
    msg["From"]=FROM
    msg["To"]=TO
    msg["Subject"]=SUBJECT
    msg['Date']=formatdate(localtime=True)

    #attach a file
    part = MIMEBase('application',"octet-stream")
    part.set_payload( open(filePath,"rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(filePath))
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('yuqiaoyan@gmail.com','m3ntos')
        ##BODY=string.join((
    ##        "From: %s" % FROM,
    ##        "To: %s" % TO,
    ##        "Subject: %s" % SUBJECT,
    ##        "",
    ##        text
    ##        ), "\r\n")
    try:
        failed = server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception, e:
        errorMSG = "Unable to send email. Error: %s" % str(e)

##    server.sendmail(FROM,[TO],BODY)
##    server.quit()


def email_example():
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # me == my email address
    # you == recipient's email address
    me = "yubonnie@umich.edu"
    you = "yuqiaoyan@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
##    s = smtplib.SMTP('localhost')
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('yuqiaoyan@gmail.com','m3ntos')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()


def main():
    email_example()

if __name__ == '__main__':
    main()
