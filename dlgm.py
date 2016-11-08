import imaplib
import email

print('|---------------------------|\n')
print('|----Custom email search----|\n')
print('|---------------------------|\n')

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
conn.login("drharby2010", "56235623")
conn.select()
#OR operator only accepts two parameters as per RFC definitions
typ, data = conn.search(None,'(OR (Subject "Home Depot") (OR (Subject "Netflix") (Subject "1800flowers")))')
index = 0;
fileTitle = 'mail'

try:
    for mail in data[0].split():
        f = open(fileTitle+str(mail), 'w')
        typ, data = conn.fetch(mail, '(RFC822)')
        body = data[0][1]
        f.write(body)
        f.close()
        fileTitle = fileTitle[:4]
        index+=1
finally:
    try: 
        conn.close()
    except:
        pass
    conn.logout()
print('[==================] OK')
