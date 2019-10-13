import imaplib, email, smtplib
import sqlite3
from email.header import decode_header
import os


def GetBody(email_message):
    if email_message.is_multipart():
        for payload in email_message.get_payload():
            payload = str(payload)
            payloadSplitted = payload.split("UTF-8")
            return payloadSplitted[1]
    else:
        return email_message.get_payload(None, True)


def GetSender(email_message): 
    fromData = email_message['From']
    fromDataSplittedList = fromData.split("<")
    sender = fromDataSplittedList[1]
    sender = sender[:-1] #deletes '>' at the end of string
    return sender

def GetTitle(email_message):
    return email_message['Subject']


def SendMail(user, password, subject, body, sendMailAddress):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user, password)
        
        msg = f'Subject:{subject} \n\n {body}'
        smtp.sendmail(user, sendMailAddress, msg)
        return("Mail sended!")


def Dbcon(): 
    condb = sqlite3.connect("mailapp.db")
    cur = condb.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inbox(id INTEGER PRIMARY KEY, sender TEXT,title TEXT,body TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS sendbox(id INTEGER PRIMARY KEY, reciever TEXT,title TEXT,body TEXT)")
    condb.commit()
    condb.close()


def Insert(tableName, contactName, title, body):
    isExist = False
    condb = sqlite3.connect("mailapp.db")
    cur = condb.cursor()
    if(tableName == "inbox"):
        if (ViewAll('inbox') != ""):
            for row in ViewAll('inbox'):
                if(row[1] == contactName and row[2] == title and row[3] == body):
                    isExist = True
        if(not isExist):
            cur.execute("INSERT Into inbox VALUES(NULL,?,?,?)",(contactName,title,body))
    
    if(tableName == "sendbox"):
        if (ViewAll('sendbox') != ""):
            for row in ViewAll('sendbox'):
                if(row[1] == contactName and row[2] == title and row[3] == body):
                    isExist = True
        if(not isExist):
            cur.execute("INSERT Into sendbox VALUES(NULL,?,?,?)",(contactName,title,body))
    
    condb.commit()
    condb.close()


def Delete(tableName, id):
    condb = sqlite3.connect("mailapp.db")
    cur = condb.cursor()
    if(tableName == "inbox"):
        cur.execute("DELETE FROM inbox Where id = ?",(id,))
    elif(tableName == "sendbox"):
        cur.execute("DELETE FROM sendbox Where id = ?",(id,))
    condb.commit()
    condb.close()
    return ("The Mail is deleted")


def View(tableName, id):
    condb = sqlite3.connect("mailapp.db")
    cur = condb.cursor()
    if(tableName == "inbox"):
        cur.execute("SELECT * FROM inbox WHERE id = ?",(id,))
        row = cur.fetchall()
    if(tableName == "sendbox"):
        cur.execute("SELECT * FROM sendbox WHERE id = ?",(id,))
        row = cur.fetchall()
    return row


def ViewAll(tableName):
    condb = sqlite3.connect("mailapp.db")
    cur = condb.cursor()
    if(tableName == "inbox"):
        cur.execute("SELECT * FROM inbox")
        rows = cur.fetchall()
    elif(tableName == "sendbox"):
        cur.execute("SELECT * FROM sendbox")
        rows = cur.fetchall()
    condb.close()
    return rows


def ViewHeader(tableName):
    condb = sqlite3.connect("mailapp.db")
    cur = condb.cursor()
    if(tableName == "inbox"):
        cur.execute("SELECT id,sender,title FROM inbox")
        rows = cur.fetchall()
    elif(tableName == "sendbox"):
        cur.execute("SELECT id,title FROM sendbox")
        rows = cur.fetchall()
    condb.close()
    return rows


def Login(user, password):
    con = imaplib.IMAP4_SSL("imap.gmail.com")
    con.login(user, password)
    con.select("INBOX")
    inboxList = []
    sentList = []
    result, data = con.search(None, "ALL")
    for num in data[0].split():
        result, data = con.fetch(num, '(RFC822)')
        if (result != 'OK'):
            return "error cannot fetch mail"

        raw = (data[0][1].decode("utf-8"))
        email_message = email.message_from_string(raw)
        inboxList.append(email_message)
        sender = GetSender(email_message)
        title = GetTitle(email_message)
        body = GetBody(email_message)
        Insert("inbox", sender, title, body)
        
    con.select('"[Gmail]/Sent Mail"')
    result, data = con.search(None, "ALL")
    for num in data[0].split():
        result, data = con.fetch(num, '(RFC822)')
        if (result != 'OK'):
            print=("Error cannot fetch mail",num)
            return

        raw = (data[0][1].decode("utf-8"))
        email_message = email.message_from_string(raw)
        sentList.append(email_message)
        title = GetTitle(email_message)
        body = GetBody(email_message)
        Insert("sendbox","",title,body)
   
    return "succesfull login"




debugger = "debugger" #can be used with breakpoint for not exiting! 