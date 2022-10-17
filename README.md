# Capstone Project

A health institute maintains the records of patient in following way. It collects general info from one datasource and medical info from another datasource. From these 2 data-sources it then combines the data and does filtering, sorting and storing  the data to common data-warehouse. And at regular intervals it generates final results for further analysis

STEPS TO PERFORM: 

1. Collect raw data from 2 data-sources (local) and git

2. Do analysis on that combined data. Filtering and Sorting

3. Send to database

4. Retrieve back few records from DB

5. Create a file and save


Try below for combining both csv files

`csvjoin -c "ID,ID" --left survey-lung-cancer-gen.csv survey-lung-cancer-other.csv > survey-lung-cancer.csv`


Do filtering with awk and convert txt to csv like below

`awk -F, '{ if($3>70) print $1,$2,$3,$17; }' survey-lung-cancer.csv > survey-lung-cancer-filtered.txt`

`sed 's/ \+/,/g' survey-lung-cancer-filtered.txt > survey-lung-cancer-filtered.csv`


Make db and table in MySql

```
$ sudo service mysql start
$ sudo service mysql start
$ sudo mysql

mysql> create user 'suuser'@'localhost' identified by 'easypass';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'suuser'@'localhost' WITH GRANT OPTION;
Query OK, 0 rows affected (0.29 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.06 sec)

mysql> SHOW GRANTS FOR 'demo1'@'localhost';

mysql> CREATE DATABASE CancerDB;
Query OK, 1 row affected (0.22 sec)

mysql> USE CancerDB
Database changed

mysql> CREATE TABLE LungCancer(
ID int,
Gender varchar(255),
Age int,
LUNG_CANCER varchar(255)
);

mysql> select * from LungCancer;
```

For storing filtered data to DB
Run `data_storage.py` file


For retriving data 

`sql2csv --db 'mysql+mysqlconnector://suuser:easypass@localhost/CancerDB?charset=utf8' --query "select * from LungCancer where Gender='M'" | csvlook > final_result`
