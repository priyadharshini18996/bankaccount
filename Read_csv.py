import csv 
f=open('university_records.csv','r')
data=csv.reader(f)
for x in data:
	print (x)
f.close()
