import smtplib 

def event_mail(x,y):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("", '') 

    msg = f"Subject: Food kitchen event\n\n{y}"

    server.sendmail(
        "NJ12jonathan@gmail.com",
        f"{x}",
        msg
    )
    server.quit()
