import csv, glob, os, sys


# updateDB.py reads outstanding emails, scans for AFROTC requests, and updates the live database, while clearing the directory afterwards.

path = "smallset"
print "Current path directory %s" % path
os.chdir(path)
pFrom = pTo = pSub = pDate = fileName = False
numCol = 1
output = 'defaulFile.csv'
for arg in sys.argv:
    if (arg == '-h'):
        print('usage: \n-f parse from section\n-t parse to section\n-s parse subject section\n-d parse date section\n-h more magic\n-n <output fileName [defaults to csv]>')
    elif (arg == '-f'):
        pFrom = True
        numCol+=1
    elif (arg == '-t'):
        pTo = True
        numCol+=1
    elif (arg == '-s'):
        pSub = True
        numCol+=1
    elif (arg == '-d'):
        pDate = True
        numCol+=1
    elif (arg == '-n'):
        fileName = True
    elif (fileName):
        output = arg + '.csv'
        fileName = False
    
index = 0

data = ["0","0","0","0","0"]
for file in glob.glob('*.msg'):
#    fpath = path + '/' + file
    data[index] = file
    index+=1
    print('reading file:' + file)
    with open(file) as fp:
        for line in fp:
            if 'From:' in line[:5] and pFrom and index < numCol:        
                data[index] = line
                index+=1
            if 'To:' in line[:3] and pTo and index < numCol:
                data[index] = line
                index+=1
            if 'Subject:' in line[:8] and pSub and index < numCol:
                data[index] = line
                index+=1
            if 'Date:' in line[:5] and pDate and index < numCol:
                data[index] = line
                index+=1
#            with open(output, 'rb') as csvfile:
#                spamreader = csv.reader(csvfile, delimiter= ',', quotechar='"')
#                for row in spamreader:
#                     print ','.join(row)
#
    with open(output, 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([data[0]] + [data[1]] + [data[2]] + [data[3]] + [data[4]])
    index = 0
