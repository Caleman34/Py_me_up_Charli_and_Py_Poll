#Import os module and csv reader
import os
import csv

#lists to store data
PyPoll_Data = os.path.join('Resources', 'PyPoll_Data.csv')

#reading csv file with specified delimiter and variable that holds contents
with open(PyPoll_Data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =',')
    
    #read the header row first
    csv_header = next(csv_reader)
    
    #create empty dictionaries
    voteCount = {}
    candidateVotes = {}

    #create a variable to hold vote count
    totalVote = 0
    
    #read through the rows of data after the header
    for row in csv_reader:

