import csv

with open('testCSV.csv','r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_test.csv','w') as new_file:
		csv_writer=csv.writer(new_file,delimiter='-')
		for line in csv_reader:
			csv.writerrow(line)
			