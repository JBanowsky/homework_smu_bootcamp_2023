# Code for opening the csv files was taken directly from class
import os
import csv

# Set path for file (path is set from within PyBank folder found in submission)
budget_data_csv = "Resources/budget_data.csv"

# Read in the CSV file
with open(budget_data_csv) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row from csv
    csv_header = next(csvreader)
    
    # Create lists to store the given month, profit/losses, and change per month from the csv file.
    month = []
    balance = []
    change = []

    # ill lists for the given month and profit/losses (append learned in class activity)
    for row in csvreader:
        month.append(row[0])     
        balance.append((row[1]))
    
    # calculations for total balance and changes per month
    total_balance = 0

    # for loop will will run through full list in balance
    for i in range(len(balance)):
        total_balance += int(balance[i])

        #fills the change list with and inputs '0' for the initial value so code will run all integers, all others are added to change list
        if i <= 0:
            change.append(0) 
        else:
            change.append(int(balance[i])-int(balance[i-1]))

    # calculation for average change; the -1 is to account for the skipping of the initial value
    avg_change = sum(change)/(len(change)-1)

    # uses built in functions to find the required information for the assignment: greatest increase and decreas and total months.
    greatest_inc = max(change)
    greatest_dec = min(change)
    total_month = len(month)
    
    # Writes lines for the required summary text file (text code as variable list shown in class activity)
    prt_out = [
        f"Financial Analysis\n",
        f"---------------\n",
        f"Total Months: {total_month}\n",
        f"Total: ${total_balance}\n",
        f"Average Change: ${round(avg_change,2)}\n",
        f"Greatest Increase in Profits: {month[change.index(greatest_inc)]}, ${round(greatest_inc, 2)}\n",
        f"Greatest Decrease in Profits: {month[change.index(greatest_dec)]}, ${round(greatest_dec, 2)}"]
    
    # terminal display of the summary (for loop learned in class activity)
    for prt_lines in prt_out:
        print(prt_lines)
    
    # creates a text file to display the summary
    # resource by David Fagbuyiro used to understand and complete code for text file https://www.freecodecamp.org/news/file-handling-in-python/ 
    txt_file = open("Analysis/PyBankFinalAnalysis.txt","w")
    txt_file.writelines(prt_out)
    txt_file.close()