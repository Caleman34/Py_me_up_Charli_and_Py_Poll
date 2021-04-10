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
      
      #calculate the average change of profit/losses for entire period
      average_change = total_profit_losses / totalMonths

      #calculate max increase
      max_profit = max(profit_losses)
      index_max = profit_losses.index(max_profit)
      max_month = months[index_max]
    
      #calculate max decrease
      min_profit = min(profit_losses)
      index_min = profit_losses.index(min_profit)
      min_month = months[index_min]

    #create variable financial analysis for output to be printed and exported
    financial_analysis = (f'''Financial Analysis
    -----------------
    Total Months: {totalMonths}
    Total: ${total_profit_losses}
    Average Change: ${average_change: .2f}
    Greatest increase in profits: {max_month} (${max_profit})
    Greatest decrease in profits: {min_month} (${min_profit})''')
   
    #print out analysis
    print(financial_analysis)
    
    #create file and export financial analysis
    output_path = os.path.join('Analysis', 'financial_analysis.txt')
    
    with open(output_path, 'w') as txtFile:
        txtFile.write(financial_analysis)

    txtFile.close()


