import os
import csv

print 'Writing into the file : \n'

filename = '/var/jenkins_home/dumps/dump_info.csv'


with file(filename,'a') as fp:
	csv_writer = csv.writer(fp,delimiter=',')
	csv_writer.writerow(['20190917','delphix.com','config','ffffhhfhfjksfks','passphrase']) 

print 'Reading from the file : \n'
with file(filename,'r') as fp2:
	for line in fp2.read().splitlines():
		print line

