import os
import csv

#import file
filename=r"Starter_Code\PyPoll\Resources\election_data.csv"

#declare variables
voter_id=[]
cands_list=[]
cands=[]
cands_votes={}
total_votes=0
name=""

#read file: 
with open(filename, 'r') as csv_file: 
    csvreader=csv.reader(csv_file)
    header=next(csvreader)

#total votes
    for row in csvreader: 
        total_votes=(total_votes+1)
 #populate unique candiate       
        candiates=(row[2])
        if candiates not in cands_list:
            cands_list.append(candiates)
    # print(cands_list)    
    # print(f'{voter_id}')
    # print(f'{candiates}')

#todo: 
#tally up votes by candiate 
#calculate vote % by candidate (candiate votes / total_votes)
#winner (max of candiate votes)


# final print: 
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")

# print("----------------------------")
# print("Charles Casper Stockham:"  )
# print("Diana DeGette:" )
# print("Raymon Anthony Doane:")
# print("----------------------------")
# print("Winner:")
# print("----------------------------")
    