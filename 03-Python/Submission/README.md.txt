SMU_Bootcamp_2023_HW_3
by John Banowsky

03-Python-Scripting/Submission

This activity is the SMU Boot Camp Module 3 Challenge. 
In this module assignment, I used Python to analyze 2 seperate csv files: 
budget_data.csv (PyBank) and election_data.csv (PyPoll)

Most of the code was resourced by the SMU Bootcamp material.

Chronologically, I completed them in order of PyBank first and PyPoll second. 
*****************************************************************************

PyBank
******
Code found in PyBank/main.py
CSV file in PyBank/Resources/budget_data.csv
Output file in PyBank/Analysis/PyBankFinalAnalysis.txt


Activity Summary:
My PyBank code takes the profit/losses value from each month and calculates the total profit/losses at the end the time frame.
I also calculate the change between months. The data was pre-sorted without any gaps.
It also tracks and outputs the months with the greatest monthly increase or decrease.


Code Summary:
The code starts with locating the csv file using code taught during the course. It includes splitting data on commas and skipping the default headers in the csv file.

I use lists and a for loop to pull and store the data from the csv: Date in yr-month (month) and profit/losses column (balance).
I also create a list called change to store the calculation for the change in profit/losses per month.
To fill the change list, I use a for loop to go through the balance list and calculate the the balance for the current index (i) and the previous one (i-1).
I account for the first month not having a change with an if loop that stores 0 for a month without a change. I ignore the 0 in the mean calculation.
Inside the for loop, I also calculate the variable total_balance to add the balance each index as an int to the previous balance.  

I use the max, min and len functions to fill in the final data analysis.

I print the anaylsis in the terminal using a method taught in class to save the text into a list and print from a for loop.

I create and write a text file in the Analysis folder.
I researched online and used an article from David Fagbuyiro to understand the text file features of python. 
https://www.freecodecamp.org/news/file-handling-in-python/ 


Code Logic:
This code used basic logic that I normally use in Excel. Read the column, use the values in columns, print the values from the same row.
I found everything to be straight forward except for the text file creation and writing. 
****************************************************************************************

PyPoll
******
Code found in PyPoll/main.py
CSV file in PyPoll/Resources/election_data.csv
Output file in PyPoll/Analysis/PyPollElectionResults.txt


Activity Summary:
My PyPoll code reads through the cvs files candidate column as votes to identify the winner. 
The code identifies the number of candidates and totals the numbers of votes each receives.
It displays each candidate, the percent of votes they receive and their total votes.
The winner is also shown.


Code Summary:
The code starts with locating the csv file using code taught during the course. It includes splitting data on commas and skipping the default headers in the csv file.

Like the previous activity, I use a list and for loop to store the candidates into a list of votes. 
This is the same time I calculate the number of votes using the length function. 
    
I use the set function to store unique values from the vote list. 
The set feature specifically gets rid of duplicates.
I then use the list feature to get a list of the unique candidates.

I create dictionaries to store an unknown number of candidates with a unique index in order to save the values to specific candidates.
The code to store unspecified number of candidates with their name, votes, and percentage was inspired by:
https://pythonprinciples.com/ask/how-do-you-create-a-variable-number-of-variables/
The strategy uses a for loop and %d to store an index number per candidate. 
During the loop, I fill the dictionaries with the index number and a particular data type: Candidate name, total votes and percent of votes.
I also use an if/elif statement to identify the winner by:
storing a winner count variable if a candidate has the highest total count and a winner variable with that candidate.

I use the same method to print the anaylsis in the terminal as before to save the text into a list and print from a for loop. 
However, the method works only for the non-variable information.
I use a for loop to display the candidate index specific text lines.

I create and write a text file in the Analysis folder the same way as before but with an extra for loop for the candidate index specific information.
This is the same strategy found from David Fagbuyiro. 
https://www.freecodecamp.org/news/file-handling-in-python/


Code Logic:
This activity takes very little effort in Excel by identifying the unique stings in the Candidates column and then counting just those names. 
To duplicate this process, I thought to store the unique values in a list and then reference those values.
I could not do the calculations like I did in the PyBank activity because I could not figure out how to reference the data from one list to the other.
I worked around this with the dictionaries, but not until I found a way to account for reading an unknown set of cadidates.
By using the %d, I was able to store an index for each unique candidate to then do a store the calculations.
It worked. It feels bulky. I couldn't think of a more simple way.