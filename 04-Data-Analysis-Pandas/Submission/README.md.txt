SMU_Bootcamp_2023_HW_4
by John Banowsky

04-Data-Analysis-Pandas/Submission

This activity is the SMU Boot Camp Module 4 Challenge. 
In this module assignment, I used Pandas DataFrames in Jupyter Notebook to analyze 2 csv files: 
schools_complete.csv and students_complete.csv

Most of the code was resourced by the SMU Bootcamp material and the presented starter code.
*****************************************************************************

PyCity Schools Analysis
******
Code found in PyCitySchools/PyCitySchools.ipynb
CSV files in PyCitySchools/Resources/..

Activity Summary:
My PyCitySchools code merges to csv files into one to analyze math and reading scores of a school district, its schools, and its students. 
It individually displays the district data as a data frame.
It then creates and displays a data frame of calculations for individual schools.
It ranks the highest 5 and lowest 5 schools by their Overall Passing percentage.
From there it breaks down the testing data into Math scores and Reading scores by grade level.
It closes by creating 3 new data frame to sort scores by budget size per student, total student population and school type.

Code Summary:
The starter code for this activity is very straightforward and guides most of the structure for the challenge. 
They merge of the two csv files was given. 

The code uses basics functions to then sort and calculate the data to create a District Summary
It uses numerical functions (sum, mean, etc.) for the numerical analysis.
It rounds grade values and money values to 2 decimal places to follow real world values.
It runs functions such as unique.size and .count for the categorical data.
The structure of my data frame codes was taught by the professor Alex Booth during class.

The School Summary uses groupbys to and similar functions as previously used to create the new data frame.
The groupbys are set using the school_name data as its index to establish a list of 15 values for each column.
For the dataframe for the per_school_summary, it creates a copy so that the formatting does not mess with the calculations further down.
Using the sort_values function, the code identifies the 5 best and worst performing schools overall.

The code then continues by sorting math and reading grades but class grades from the merged data frame.

It is followed using bins to sort the data even further into categories of budget ranges, school size and school type. 
This process followed the same sorting and formatting as the previous sections.

The analysis of the data can be found at the top of the code file.

EXTRA Code:
To help with the analysis, I included a version of the data frame that sorts the schools so I could compare types.
The first sorts by budget per student.
The second sort is by total students.
This section allows me to discern the difference between charter school and district schools.
