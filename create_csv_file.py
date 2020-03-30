import csv

def create_csv_file():
    records = [
        {'id':'1','firstname':'priya','lastname':'mohan'},
        {'id':'2','firstname':'preethi','lastname':'karthi'},
        {'id':'3','firstname':'pravi','lastname':'prakash'},
        {'id':'4','firstname':'prasath','lastname':'soundary'},
        {'id':'5','firstname':'harish','lastname':'swetha'}
    ]
    csv_writer =csv.writer(open('records.csv','w'),delimiter=',')
    csv_writer.writerow(['id','firstname','lastname'])
    for record in records:
        csv_writer.writerow([record['id'],record['firstname'],record['lastname']])
def read_csv_file():
    for row in csv.reader(open('records.csv','r'),delimiter=','):
        if len(row)> 0:
            print(row[0]+' '+row[1]+' '+row[2])
def update_csv_file():
    csv_writer =csv.writer(open('records.csv','w'),delimiter=',')
    csv_writer.writerow(['6','nithya','lekha'])
     

create_csv_file()
read_csv_file()
update_csv_file()