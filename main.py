import smtplib
import email.message
from tkinter import scrolledtext
from tkinter import *

def sendEmail():
    corpse = """
    <p>"""+TextArea.get("1.0",'end-1c')+"""</p>
    """

    msg = email.message.Message()
    msg["Subject"] = Subject.get()
    msg["From"] = Email.get()
    msg["To"] = To.get()
    password = Password.get()
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpse)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    print("Email was been sended")


gui = Tk()
gui.title("Simplest Email Sender Ever")

Email = Entry(gui, width=40)
Password = Entry(gui, width=40)
Subject = Entry(gui, width=45)
To = Entry(gui, width=45)
MessageText = Label(gui, text="Your message here:")
TextArea = scrolledtext.ScrolledText(gui, wrap=WORD, width=45, height=8, font=("Calibri",12))
Send = Button(gui, text='Send', width=30, height=5, command=sendEmail)

Email.insert(0,'Your Email Here')
Password.insert(0, 'Your Password Here')
To.insert(0,'Email to send')
Subject.insert(0,'Subject here')

Email.grid(row=0,column=0)
Subject.grid(row=1,column=1)
Password.grid(row=1,column=0)
MessageText.grid(row=2,column=1)
TextArea.grid(row=3,column=1)
To.grid(row=0,column=1)
Send.grid(row=3,column=0)


gui.mainloop()