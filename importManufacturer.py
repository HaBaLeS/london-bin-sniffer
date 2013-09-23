import dbutils
import csv


ds = dbutils.SqliteDataStore('sniffer.db')

with open('manu.txt', 'rb') as csvfile:
    man = csv.reader(csvfile, delimiter='\t')
    for line in man:
        line[0] = line[0].replace('-',':')
        line[1] = line[1].decode('utf-8')
        ds.execute('insert into mac2Man values (?,?)',line)
    ds.commit()
