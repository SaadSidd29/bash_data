#!/bin/bash


echo "Fetch the data from Data-source"

wget -O /mnt/s/demo1/final_project/bash_data/survey-lung-cancer-gen.xlsx  https://github.com/SaadSidd29/bash_data/blob/main/survey-lung-cancer-gen.xlsx?raw=true

if [ -e survey-lung-cancer-gen.xlsx ]
then
echo "Convert to csv"
in2csv survey-lung-cancer-gen.xlsx > survey-lung-cancer-gen.csv
echo "Checking for error"
check=`csvclean -n survey-lung-cancer-gen.csv | grep "No errors" | wc -l`
if [ $check == 1 ]
then
echo "No errors are found in file"
else
echo "Check for errors"
fi

else
echo "File doesn't exists"
fi
