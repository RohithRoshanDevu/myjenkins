import os
import csv

print 'Writing into the file : \n'

with file('/dumps/dump_info.csv','a') as fp:
	csv_writer = csv.writer(fp,delimiter=',')
	csv_writer.writerow('20190917','delphix.com','config','ffffhhfhfjksfks','passphrase',) 

print 'Reading from the file : \n'
with file('/dumps/dump_info.csv','r') as fp2:
	for line in fp2.read().splitlines():
		print line

