import imaplib, email

user = "compproj1itu@gmail.com"
password = "Compproj1010"
imapUrl = "imap.gmail.com"

def GetBody(msg):
    if msg.is_multipart():
        return GetBody(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key,value,con):
    result, data = con.search(None,key,'"()"'.format(value))
    debugger = "debugger"
    return data

con = imaplib.IMAP4_SSL(imapUrl)
con.login(user, password)
con.select("INBOX")
result, data = con.fetch(b'2','(RFC822)')
raw = email.message_from_bytes(data[0][1])
print(GetBody(raw))

#search("FROM","mlkmhmtbyk@gma.com",con)

debugger = "debugger"