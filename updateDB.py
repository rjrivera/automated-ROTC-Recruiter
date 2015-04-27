import csv, glob, os, StringIO


# updateDB.py reads outstanding emails, scans for AFROTC requests, and updates the live database, while clearing the directory afterwards.

path = "/home/rjrivera/mail/new"
print "Current path directory %s" % path

os.chdir(path)
for file in glob.glob("*.cleverGirl"):
    fpath = path + '/' + file
    myFile = open(fpath).read()
    if 'AFROTC.com Request' in myFile:
        print("I think this file might be the one")
        print(myFile)
        break
os.chdir("/home/rjrivera/mail/")
with open('myTestDB.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ',', quotechar='"')

    for row in spamreader:
        print ','.join(row)
    
with open('myTestDB.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar=':', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(['Malkovich'] + ['John'])
    
    
