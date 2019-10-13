from tkinter import *   
import MailActions


def LoginCommand():
    MailActions.Dbcon()
    t5.delete('1.0',END)
    t5.insert('1.0',MailActions.Login(e1.get(),e2.get()))

    inboxList.delete(0,END)
    for row in MailActions.ViewHeader("inbox"):
        inboxList.insert(END,row)

    sendList.delete(0,END)
    for row in MailActions.ViewHeader("sendbox"):
        sendList.insert(END,row)


def ReadInboxCommand():
    index = inboxList.curselection()[0]
    selectedTuple = inboxList.get(index)
    id = selectedTuple[0]
    
    t1.delete('1.0',END)
    for item in MailActions.View('inbox',id):
        t1.insert('1.0',item)


def ReadSendboxCommand():
    index = sendList.curselection()[0]
    selectedTuple = sendList.get(index)
    id = selectedTuple[0]

    t1.delete('1.0',END)
    for item in MailActions.View('sendbox',id):
        t1.insert('1.0',item)


def DeleteInboxCommand():
    index = inboxList.curselection()[0]
    selectedTuple = sendList.get(index)
    id = selectedTuple[0]
    t5.delete('1.0',END)
    t5.insert('1.0',MailActions.Delete("inbox",id))


def DeleteSendboxCommand():
    index = sendList.curselection()[0]
    selectedTuple = sendList.get(index)
    id = selectedTuple[0]
    t5.delete('1.0',END)
    t5.insert('1.0',MailActions.Delete("sendbox",id))


def SendCommand():
    user = e1.get()
    password = e2.get()
    contactMail = t2.get('1.0',END)
    title = t3.get('1.0',END)
    body = t4.get('1.0',END)
    t5.delete('1.0',END)
    t5.insert('1.0',MailActions.SendMail(user, password, title, body, contactMail))


window=Tk()

window.wm_title("MailApp")
 

l1=Label(window,text="   ")
l1.grid(row=0,column=0)

l2=Label(window,text="Mail Address: ")
l2.grid(row=1,column=1)

mailText=StringVar()
e1=Entry(window,textvariable=mailText)
e1.grid(row=1,column=2)


l1=Label(window,text="   ")
l1.grid(row=2,column=0)

l3=Label(window,text="Password: ")
l3.grid(row=3,column=1)

passwordText=StringVar()
e2=Entry(window,textvariable=passwordText)
e2.grid(row=3,column=2)


b1=Button(window,text="LOGIN", width=20,command=LoginCommand)
b1.grid(row=1,rowspan=2,column=3)

t5=Text(window,height=3, width=20)
t5.grid(row=3,column=3)

l1=Label(window,text="   ")
l1.grid(row=4,column=0)

l1=Label(window,text="   ")
l1.grid(row=5,column=0)


l4=Label(window,text="Inbox List: ")
l4.grid(row=6,column=1)

inboxList=Listbox(window, height=10,width=60)
inboxList.grid(row=7,column=1,rowspan=6,columnspan=2)

b2=Button(window,text="READ", width=10,command=ReadInboxCommand)
b2.grid(row=7,column=3)

b3=Button(window,text="DELETE", width=10,command=DeleteInboxCommand)
b3.grid(row=8,column=3)


l5=Label(window,text="Sended Mails: ")
l5.grid(row=6,column=5)

sendList=Listbox(window, height=10,width=60)
sendList.grid(row=7,column=4,rowspan=6,columnspan=3)

l1=Label(window,text="   ")
l1.grid(row=7,column=6)

b4=Button(window,text="READ", width=10,command=ReadSendboxCommand)
b4.grid(row=7,column=6)

l1=Label(window,text="   ")
l1.grid(row=8,column=6)

b5=Button(window,text="DELETE", width=10,command=DeleteSendboxCommand)
b5.grid(row=8,column=6)

l6=Label(window,text="Read Mails: ")
l6.grid(row=18,column=1)

t1=Text(window,height=20, width=80)
t1.grid(row=20,column=1,rowspan=50,columnspan=3)


l7=Label(window,text="Write Mail: ")
l7.grid(row=14,column=5)

l7=Label(window,text="Sent to: ")
l7.grid(row=15,column=5)

t2=Text(window,height=1, width=30)
t2.grid(row=16,column=5)

l7=Label(window,text="Subject: ")
l7.grid(row=17,column=5)

t3=Text(window,height=1, width=30)
t3.grid(row=18,column=5)

l7=Label(window,text="Mail: ")
l7.grid(row=19,column=5)

t4=Text(window,height=20, width=80)
t4.grid(row=20,column=5)

b5=Button(window,text="SEND", width=10,command=SendCommand)
b5.grid(row=20,column=6)




window.mainloop() #for keeping the tkinter window
