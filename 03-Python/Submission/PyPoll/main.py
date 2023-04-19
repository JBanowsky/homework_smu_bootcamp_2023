#Code for opening the csv files was taken directly from class
import os
import csv

# Set path for file (path is set from within PyPoll folder found in submission)
election_data_csv = "Resources/election_data.csv"

# Read in the CSV file
with open(election_data_csv) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header row from csv
    csv_header = next(csvreader)
    
    #Create lists to store the votes and candidate list.
    #votes will store the entire list of votes from the csv files 3rd row.
    votes = []
    #candidate list will create a list of all the candidates that have votes.
    candidate_list = []
    
    #store the votes from the csv file to the votes list
    for row in csvreader:
        votes.append(row[2])       

    #used length of votes to find the total votes    
    total_votes = len(votes)
    
    #Use set function to stores objects with out duplicates then turn set into and ordered list for functionality
    vote_set = set(votes)
    candidate_list = (list(vote_set)) 
      
    #use dictionaries to connect the votes with the corresponding candidate 
    #code to store unspecified number of candidates with their name, votes, and percentage was inspired by
    #https://pythonprinciples.com/ask/how-do-you-create-a-variable-number-of-variables/
    
    #create dictionaries
    candidate_name = {}
    candidate_total = {}
    candidate_percent = {}
    
    #establish variable to compare votes between candidates
    winner_count = 0
    
    #from above webstie, create a loop that runs each candidate and fills dictionaries with desired values
    for i in range(len(candidate_list)):
        #stores callable string of candidates name with index value
        candidate_count = "candidate%d" % i
        candidate_name[candidate_count] = str(candidate_list[i])
        #stores number of votes for each candidate with same index value
        candidate_total[candidate_count] = votes.count(candidate_name["candidate%d"%i])
        #stores percent value for each candidate with same index value
        candidate_percent[candidate_count] = round(candidate_total["candidate%d"%i]/total_votes*100,3)
        #identify largest vote total as winner or set as tie if a tie is present
        if candidate_total["candidate%d"%i] > winner_count:
            winner_count = candidate_total["candidate%d"%i]
            winner = candidate_name["candidate%d"%i]
        elif candidate_total["candidate%d"%i] == winner_count:
            winner = "Tie"

    #Writes lines for the required summary text file
    #To accomodate loop for unknown variable of candidates the text is split into 3 parts: start, loop, end
    #create text variable of initial text that is unaffexted by loop. Used in both terminal and in text file
    txt_start = (
        f"Election Results\n",
        f"---------------\n",
        f"Total Votes: {total_votes}\n",
        f"---------------\n")
    #terminal display of starting text (for loop learned in class activity)
    for prt_lines in txt_start:
        print(prt_lines)
    
    #loop to display data
    for i in range(len(candidate_list)):
        txt1 = str(candidate_name["candidate%d"%i])
        txt2 = str(candidate_percent["candidate%d"%i])
        txt3 = str(candidate_total["candidate%d"%i])
        print(f"{txt1}: {txt2}% ({txt3})\n")
    
    #create text variable of end text that is unaffexted by loop. Used in both terminal and in text file
    txt_end = (
        f"---------------\n",
        f"Winner: {winner}\n",
        f"---------------\n")
    #terminal display of the summary
    for prt_lines in txt_end:
        print(prt_lines)

    #creates a text file to display text
    #resource by David Fagbuyiro used to understand and complete code for text file https://www.freecodecamp.org/news/file-handling-in-python/
    txt_file = open("Analysis/PyPollElectionResults.txt","w")
    #write line used for start
    txt_file.writelines(txt_start)
    #Write lines function is in loop for the variable numbers of candidates
    for i in range(len(candidate_list)):
        txt1 = str(candidate_name["candidate%d"%i])
        txt2 = str(candidate_percent["candidate%d"%i])
        txt3 = str(candidate_total["candidate%d"%i])
        txt_file.writelines(f"{txt1}: {txt2}% ({txt3})\n")
    #write line used for end
    txt_file.writelines(txt_end)
    #close the text file
    txt_file.close()



