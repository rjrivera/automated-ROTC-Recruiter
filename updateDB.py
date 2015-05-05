import csv, glob, os


# updateDB.py reads outstanding emails, scans for AFROTC requests, and updates the live database, while clearing the directory afterwards.

path = "/home/rjrivera/mail/new"
print "Current path directory %s" % path

fileCandidateInfo = ["0","0","0","0","0","0"]

os.chdir(path)
for file in glob.glob("*.cleverGirl"):
    fpath = path + '/' + file
    myFile = open(fpath).read()
    if 'AFROTC College Info Request' in myFile:
        print("I think this file might be the one")
        print(myFile)
        print("reading file again, line by line")
        fileCurrentLine = "BANANA"
        with open(fpath) as fp:
            for line in fp:
                print("currently at this line: " + line)
                if 'College:' in line:
                    sizeOfLine = len(line)
                    line = line[8:sizeOfLine]
                    print(line)
                    line = line.strip()
                    print(line)
                    fileCandidateInfo[2] = line
                    print("candidate wants - " + line)
                    
                if 'Last Name:' in line:        
                    sizeOfLine = len(line)
                    line = line[10:sizeOfLine]
                    print(line)
                    line = line.strip()
                    print(line)
                    fileCandidateInfo[0] = line 
                    print("candidate last name - " + fileCandidateInfo[0])
                if 'First Name:' in line:
                    sizeOfLine = len(line)
                    line = line[11:sizeOfLine]
                    print(line)
                    line = line.strip()
                    fileCandidateInfo[1] = line
                    print("candidate first name - " + fileCandidateInfo[1])
                if 'Email Address:' in line:
                    sizeOfLine = len(line)
                    line = line[14:sizeOfLine]
                    print(line)
                    line = line.strip()
                    print(line)
                    fileCandidateInfo[3] = line
                    print("candidate EMAIL - " + fileCandidateInfo[3])
        break
os.chdir("/home/rjrivera/mail/")
with open('myTestDB.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ',', quotechar='"')

    for row in spamreader:
        print ','.join(row)
    
with open('myTestDB.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow([fileCandidateInfo[0]] + [fileCandidateInfo[1]] + [fileCandidateInfo[2]] + [fileCandidateInfo[3]])
