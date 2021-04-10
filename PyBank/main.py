#Import os module and csv reader
import os
import csv

#create variable for path to file
PyBank_Data = os.path.join('..', 'Resources', 'PyBank_Data.csv')

#reading csv file with specified delimiter and variable that holds contents
with open(PyBank_Data) as csvfile:
    PyBank_Data_reader = csv.reader(csvfile, delimiter=',')

    print(PyBank_Data_reader)

    #read the header row first
    csv_header = next(PyBank_Data_reader)
    print(f"CSV HEADER: {csv_header}")

    #read through the rows of data after the header
    for row in PyBank_Data_reader