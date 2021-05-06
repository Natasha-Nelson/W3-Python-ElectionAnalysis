# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = "election_results.csv"
# Assign a variable to save the file to a path.
file_to_save = os.path.join("W3-Python-ElectionAnalysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)



#The Types of Data We Need To Get
# Total number of votes cast
## Create a total_votes variable
## Set the variable Count the number of unique ballot IDs in the datasheet

#A complete list of candidates who received votes
## Create a new list
## Add the first candidate's name to the list
## Check the next name on the list
## If the name is not on the list, add it to the list

#Total number of votes each candidate received
## Start a new dictionary
## Create a key-value system for votes for each candidate

#Percentage of votes each candidate won
## divide the value of vote for candidate by total votes

#The winner of the election based on popular vote
## figure out which candidate has the biggest number of votes