'''import smtplib

my_email = "t66393552@gmail.com"
password ="jgvlizoptcqnnntu" #"itsmemario" <-This is the actual password.
receiver= "jstat123test@gmail.com"


with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
    connection.starttls() #making the connection secure by encrypting using TLS
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg="Hello"
    )
    print("sent")
#connection.close()

Providers:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com
'''

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
dayOfWeek = now.weekday()

print(year)

DOB = dt.datetime()#year= int, month = int, day = int, hours = 12)