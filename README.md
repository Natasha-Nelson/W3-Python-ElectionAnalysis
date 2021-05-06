# W3-Python-ElectionAnalysis

## Project Overview
The goal of this project was to analyze the results of local election to determine the winning candidate and characterize other key aspects of the voting results. In the initial phase, I created a script to verify:
  1. The total number of votes cast
  2. The list of candidates who received votes
  3. The total number of votes each candidate received 
  4. The percentage of votes cast for each candidate
  5. The election winner

In the second phase of the project, I expanded the initial script to identify:
  1. The list of counties in which votes were cast
  2. The number of votes cast in each county and percentage
  3. The county with the highest voter turnout 

## Resources
- Python 3.7
- Visual Studio Code
- Data source: election_results.csv41
- Starter code: PyPoll_Challenge_starter_code.py

## Election Results - Summary
The analysis of the election results data demonstrated that:
* There were 369,711 votes cast in this congressional election
* The county with the highest turnout was Denver with 306,055 votes
* Each county cast:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
* Each candidate received the following:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* The winning candidate was Diana DeGette with 73.8% of the vote (272,892)

## Election-Audit Summary
This script is flexible enought to be used for elections at a range of sizes and does not need to be modified based on the number of votes cast. It can be easily applied to smaller county board elections and is useful in variety of situations. The expand the scope of this analysis further, one modification that could be included is a breakdown of the number of votes each candidate received by county. This could be acheived by adding additional code in the loop initialized in line 41 with a conditional statement and mapping back to a separate dictionary for each candidate that could hold these results. From there, we can easily expand the include the percentage of each county's vote a candidate received. 
