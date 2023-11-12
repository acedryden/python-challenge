import csv
import os


filename=r'PyPoll\Resources\election_data.csv'
# name_1_list=0 


with open(filename, 'r') as csvFile:
    csvreader=csv.reader(csvFile, delimiter=',')
    header=next(csvreader)
    data=[]
    # print(csvFile)
    for row in csvreader: 
        voterid=int(row[0])
        data.append(voterid)
        # print(voterid)
        total_votes=0
        total_votes=sum(voterid)
        print(total_votes)
         #print(row[0])
        #print(row[2])
    #     namelist=str(row[2])
    #      #print(voterid)
    #     #  print(namelist)
    #     #  uniqueName=str()
    # print(sum(voterid))
         
        
        # voteCounter=0
       
        # for vote in voterid:
        #     if vote!=vote: 
        #         voteCounter=(voteCounter+1)
        #         print(voteCounter)
        # print(voterid)
       


  
  
    # name_1_list=()
    # for name in namelist:
    #      if name==name:
    #         name_exists=True
    #      if name_exists==False:
    #          namelist.append(name)
    #      if row[2]==namelist[0]:
    #          name_1_list.append(namelist[0])
    #          name_1_votes=len(name_1_list)
    #          print(name_1_list)

       




#total votes: 

#list of candiates: 

#total of votes by candiate: 

#candiate %: 
#will be votes by candiate / total votes
#canA%: (canA.votes/total.votes *100)
#canB%: (canB.votes/total.votes *100)
#canC%: (canC.votes/total.votes *100)

#winner: 
#if statement? ie if candiate A > candiate B, candiate A is winner, etc. 

#final print: 
# print("Election Results")
# print("----------------------------")
# print("Total Votes:" + )
# print("----------------------------")
# print("Charles Casper Stockham:"  )
# print("Diana DeGette:" )
# print("Raymon Anthony Doane:")
# print("----------------------------")
#print("Winner:")
# print("----------------------------")
    

