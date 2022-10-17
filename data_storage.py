import mysql.connector
import csv

mydb = mysql.connector.connect(
                  host="localhost",
                            database='CancerDB',
                                      user='suuser',
                                                password='easypass'
                                                              )

print(mydb)
print("Congrats DB object created")


with open('survey-lung-cancer-filtered.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                sql=f"INSERT INTO LungCancer (ID,GENDER,AGE,LUNG_CANCER) VALUES ({row[0]},'{row[1]}',{row[2]},'{row[3]}')"
                print(sql)
                mycursor = mydb.cursor()
                mycursor.execute(sql)
                mydb.commit()
                line_count += 1
        print(f'Processed {line_count} lines.')

