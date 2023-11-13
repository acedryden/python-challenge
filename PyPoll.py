import os
import csv

#import file
filename=r"Starter_Code\PyPoll\Resources\election_data.csv"

#declare variables
cands_list=[]
total_votes=0
can1_votes=0
can2_votes=0
can3_votes=0
winner=""
winner_num=0

#read file & assign header: 
with open(filename, 'r') as csv_file: 
    csvreader=csv.reader(csv_file)
    header=next(csvreader)

#total votes
    for row in csvreader: 
        total_votes=(total_votes+1)
        unique_votes=row[0]

#populate unique candiate       
        candiates=(row[2])
        if candiates not in cands_list:
            cands_list.append(candiates)
  
#tally up votes by candiate 
        if candiates=="Charles Casper Stockham":
            can1_votes=(can1_votes+1)
        elif candiates=="Diana DeGette":
            can2_votes=(can2_votes+1)
        else:
            can3_votes=(can3_votes+1)
  

#calculate vote % by candidate & round to 3 decimal places

can1_share=((can1_votes/total_votes) *100)
can1_share=(round(float(can1_share),3))
can2_share=((can2_votes/total_votes) *100)
can2_share=(round(float(can2_share),3))
can3_share=((can3_votes/total_votes) *100)
can3_share=(round(float(can3_share),3))

#calculate winner
if can1_votes > winner_num:
    winner="Charles Casper Stockham"
    winner_num=can1_votes
if can2_votes>winner_num:
    winner="Diana DeGee"
    winner_num=can2_votes
if can3_votes>winner_num:
    winner="Raymon Anthony Doane"
    winner_num=can3_votes


#write to .txt file
OUTPUT_PATH=os.path.join("pypoll_analysis.txt")

with open(OUTPUT_PATH, 'w') as textfile: 

    election_results=(
        f"\n\nElection Results\n"
        f"\n------------------------\n"
        f"\nTotal Votes: {total_votes}\n"
        f"\n-----------------------\n"
        f"\nCharles Casper Stockham: {can1_share}% ({can1_votes})\n"
        f"\nDiana DeGette: {can2_share}% ({can2_votes})\n"
        f"\nRaymon Anthony Doane: {can3_share}% ({can3_votes})\n"
        f"\n------------------------\n"
        f"\nWinner: {winner} \n"
        f"\n------------------------\n")
    print(election_results, end="")
     
    textfile.write(election_results)

    