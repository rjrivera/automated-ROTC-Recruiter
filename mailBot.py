import subprocess
import sys

cmdSSMTP = "mutt -s \"AFROTC Lead Update\" -a myTestDB.csv -- afrotc.det365@gmail.com < reportMail.txt"

cmdRM = "rm -r new/*"

p = subprocess.Popen(cmdSSMTP, shell = True, stderr=subprocess.PIPE)

while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()

p = subprocess.Popen(cmdRM, shell = True, stderr= subprocess.PIPE)

while True:
    out = p.stderr.read(1)
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()


print "*** Mailbot.py executed ***"
