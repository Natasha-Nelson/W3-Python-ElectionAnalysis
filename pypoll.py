<<<<<<< HEAD
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = "election_results.csv"
# Assign a variable to save the file to a path.
file_to_save = "election_analysis.txt"

#Set a Variable to Count Total Number of Votes
total_Votes = 0

#Create a List of Candidates
candidate_list = []

#create a Dictionary for Vote Counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        #increase vote count 
        total_Votes += 1

        #Find candidate names 
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            # add candidate names to the list
            candidate_list.append(candidate_name)
            #initialize candidate votes at zero
            candidate_votes[candidate_name] = 0
        #start adding votes for each candidate
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save,'w') as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_Votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.   
        txt_file.write(election_results)

        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            # divide the value of vote for candidate by total votes
            vote_percentage = float(votes) / float(total_Votes) * 100

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_percentage = vote_percentage
                winning_count = votes
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
=======
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = "election_results.csv"
# Assign a variable to save the file to a path.
file_to_save = "election_analysis.txt"

#Set a Variable to Count Total Number of Votes
total_Votes = 0

#Create a List of Candidates
candidate_list = []

#create a Dictionary for Vote Counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        #increase vote count 
        total_Votes += 1

        #Find candidate names 
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            # add candidate names to the list
            candidate_list.append(candidate_name)
            #initialize candidate votes at zero
            candidate_votes[candidate_name] = 0
        #start adding votes for each candidate
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save,'w') as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_Votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.   
        txt_file.write(election_results)

        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            # divide the value of vote for candidate by total votes
            vote_percentage = float(votes) / float(total_Votes) * 100

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_percentage = vote_percentage
                winning_count = votes
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
>>>>>>> 94222bd45285145d27f9ece3391f668b11f35bbc
