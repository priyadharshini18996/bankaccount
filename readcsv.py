import csv 

filename = "university_records.csv"

#  titles and rows list 
# fields = [] 
rows 

# readS csv file 
with open(filename, 'r') as csvfile: 
	# CSV reader object 
	csvreader = csv.reader(csvfile) 
	

	for row in csvreader: 
		rows.append(row) 
print(rows)
 
# 	print("Total no. of rows: %d"%(csvreader.line_num)) 

# # print('Field names are:' + ', '.join(field for field in fields)) 


# print('\nFirst 5 rows are:\n') 
# for row in rows[:4]: 
# 	# row of each column
# 	for col in row: 
# 		print(col), 
# 	print('\n') 


