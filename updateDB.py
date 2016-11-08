import csv, glob, os


# updateDB.py reads outstanding emails, scans for AFROTC requests, and updates the live database, while clearing the directory afterwards.

path = "rjrivera/automated-ROTC-Recruiter"
print "Current path directory %s" % path
serverDomain = "VirtualBox"
fileCandidateInfo = ["0","0","0","0","0","0", "0", "0","0","0","0","0","0"]

os.chdir(path)
for file in glob.glob("*."+serverDomain):
    fpath = path + '/' + file
    myFile = open(fpath).read()
    if 'AFROTC College Info Request' in myFile:
        
        print("reading file again, line by line")
        with open(fpath) as fp:
            for line in fp:
                print("currently at this line: " + line)
                    
                if 'Last Name:' in line:        
                    sizeOfLine = len(line)
                    line = line[10:sizeOfLine]
                    print(line)
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    print(line)
                    fileCandidateInfo[0] = line 
                    print("candidate last name - " + fileCandidateInfo[0])
                if 'First Name:' in line:
                    sizeOfLine = len(line)
                    line = line[11:sizeOfLine]
                    print(line)
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[1] = line
                    print("candidate first name - " + fileCandidateInfo[1])
                if 'College:' in line:
                    line = line[8:len(line)]
                    print(line)
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4] 
                    print(line)
                    fileCandidateInfo[2] = line
                    print("candidate wants - " + line)
                if 'Email Address:' in line:
                    line = line[14:len(line)]
                    print(line)
                    line = line.strip()
                    line = line[0:len(line)-4]
                    print(line)
                    fileCandidateInfo[3] = line
                    print("candidate EMAIL - " + fileCandidateInfo[3])
                if 'Mailing Address:' in line:
                    line = line[16:len(line)]
                    line = line.strip()
                    if '=0A=' in line:    
                        line = line[0:len(line)-4]
                    fileCandidateInfo[4] = line
                    print("candidate ADDRESS - " + fileCandidateInfo[4])
                if 'City:' in line:
                    line = line[5:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[5] = line
                    print("candidate CITY - " + fileCandidateInfo[5])
                if 'State' in line:
                    line = line[5:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[6] = line
                    print("candidate STATE - " + fileCandidateInfo[6])
        
                if 'ZIP:' in line:
                    line = line[4:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[7] = line
                    print("candidate ZIP - " + fileCandidateInfo[7])

                if 'Phone:' in line: 
                    line = line[6:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[8] = line
                    print("candidate PHONE - " + fileCandidateInfo[8])
                if 'SAT Score:' in line:
                    line = line[10:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[9] = line
                    print("candidate SAT Score - " + fileCandidateInfo[9])
    
                if 'ACT Score:' in line:
                    line = line[10:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[10] = line
                    print("candidate ACT Score - " + fileCandidateInfo[10])
  
                if 'GPA Score:' in line:
                    line = line[10:len(line)]
                    line = line.strip()
                    if '=0A=' in line:
                        line = line[0:len(line)-4]
                    fileCandidateInfo[11] = line
                    print("candidate GPA - " + fileCandidateInfo[11])
                    os.chdir("/home/rjrivera/mail/")
                    with open('myTestDB.csv', 'rb') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter= ',', quotechar='"')

                        for row in spamreader:
                            print ','.join(row)

                    with open('myTestDB.csv', 'a') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        spamwriter.writerow([fileCandidateInfo[0]] + [fileCandidateInfo[1]] + [fileCandidateInfo[2]] + [fileCandidateInfo[3]] + [fileCandidateInfo[4]] + [fileCandidateInfo[5]] + [fileCandidateInfo[6]] + [fileCandidateInfo[7]] + [fileCandidateInfo[8]] + [fileCandidateInfo[9]] + [fileCandidateInfo[10]] + [fileCandidateInfo[11]])
        
