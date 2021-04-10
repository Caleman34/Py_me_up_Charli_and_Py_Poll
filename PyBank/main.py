#Import os module and csv reader
import os
import csv

#lists to store data
PyBank_Data = os.path.join('Resources', 'PyBank_Data.csv')

#reading csv file with specified delimiter and variable that holds contents
with open(PyBank_Data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =',')
    
    #read the header row first
    csv_header = next(csv_reader)
    
    #create variables with empty lists
    months = []
    profit_losses = []


    #read through the rows of data after the header
    for row in csv_reader:
      #add row count to months for number of "months" in data set
      months.append(row[0])
      #calculate length of "totalMonths" aka total number of rows after the header
      totalMonths = (len(months)) 
      
      #add profit/losses to sum list
      profit_losses.append(row[1])
       #sum of total profit/losses
      total_profit_losses = sum(profit_losses)
     
         
    
    #print data results
    print(totalMonths)
    print(total_profit_losses)
      

