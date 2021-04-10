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
      
      #add profit/losses in column 1 to ptofit/loses variable empty list
      profit_losses.append(int(row[1]))
       #sum of total profit/losses variable
      total_profit_losses = sum(profit_losses)
     
         
    
    #create variable financial analysis for output to be printed and exported
    financial_analysis = (f'''Financial Analysis
    -----------------
    Total Months: {totalMonths}
    Total: ${total_profit_losses}
    Average Change: 
    Greatest increase in profits:
    Greatest decrease in profits: ''')
   
    #print out analysis
    print(financial_analysis)
    
    #create file and export financial analysis
    output_path = os.path.join('Analysis', 'financial_analysis.txt')
    
    with open(output_path, 'w') as txtFile:
        txtFile.write(financial_analysis)

    txtFile.close()


