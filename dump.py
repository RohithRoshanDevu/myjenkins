import os
import csv

with file('/dumps/dump_info.csv,'a') as fp:
	csv_writer = csv.writer(fp,delimiter=',')
	csv_writer.writerow('20190917','delphix.com','config','ffffhhfhfjksfks','passphrase',) 



