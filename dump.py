import os
import csv
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


print 'Writing into the file : \n'

filename = '/var/jenkins_home/dumps/dump_info.csv'

rannum = str(random.randint(111111,999999))

ranstring = randomString(15)

ranpass = randomString(6)


with file(filename,'a') as fp:
	csv_writer = csv.writer(fp,delimiter=',')
	csv_writer.writerow([rannum,'delphix.com','config',ranstring,ranpass]) 

print 'Reading from the file : \n'
with file(filename,'r') as fp2:
	for line in fp2.read().splitlines():
		print line

