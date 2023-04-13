SMU_Bootcamp_2023_HW_2
by John Banowsky

02-VBA-Scripting/Submission

This activity is the SMU Boot Camp Module 2 Challenge. In this module assignment, I used VBA scripting to analyze generated stock market data (the data was pre-sorted alphabetically by stock and chronologically). Taking volume, the opening price, and the closing price for a stock for a year, I displayed total volume, price change and percent change as well as the stock with the largest percent increase, decrease and total volume.

Code can be found in Multiple_year_stock_code.txt

My code is structured around reading a ticker value, storing the initial opening price, and then summing its volume each line until it entcounters the last given row. Then the code stores the ending price and calculates and displays the price change and the percent change as well as calculating and displaying the total volume. The variables pertaining to price and volume are then reset and the it repreats using a for loop. In order to display the stocks with greatest value, I used conditionals to compare and store the largest increase, decrease and total volume each time the ticker value changed. I used cell formating to display the data appropriately. This code does run through each sheet in the workbook using a for loop and worksheet functions.

Most of the code was resourced by the SMU Bootcamp material.

Resources to count to last row:
https://www.wallstreetmojo.com/vba-last-row/ (given from AskBCS Learning Assistants)

Resources to Loop each worksheet:
https://trumpexcel.com/vba-worksheets/
https://support.microsoft.com/en-us/topic/macro-to-loop-through-all-worksheets-in-a-workbook-feef14e3-97cf-00e2-538b-5da40186e2b0