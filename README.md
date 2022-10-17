# Capstone Project

A health institute maintains the records of patient in following way. It collects general info from one datasource and medical info from another datasource. From these 2 data-sources it then combines the data and does filtering, sorting and storing  the data to common data-warehouse. And at regular intervals it generates final results for further analysis

STEPS TO PERFORM: 

1. Collect raw data from 2 data-sources (local) and git

2. Do analysis on that combined data. Filtering and Sorting

3. Send to database

4. Retrieve back few records from DB

5. Create a xls file and save


Try below for combining both csv files

`csvjoin -c "ID,ID" --left survey-lung-cancer-gen.csv survey-lung-cancer-other.csv > survey-lung-cancer.csv`
