#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:42:52 2023

@author: bradyogega
"""
#import Files to Run
import csv
import_file = ("/Users/bradyogega/Downloads/Starter_Code 3/PyPoll/Resources/election_data.csv")
analysis_file = ("/Users/bradyogega/Desktop/PyPoll/PyPoll_Analysis.txt")

#Set counters and empty lists
total_votes = 0

nominee_options =[]
nominee_votes ={}

winning_nominee = ""
winner_count = 0

#Read CSV convert list to dictionaries
with open(import_file) as ballot_data:
    reader = csv.DictReader(ballot_data)

#iterate through rows in CSV    
    for row in reader:
        
        total_votes = total_votes + 1
        
        nominee_name = row["Candidate"]
 
        #set conditons and append results increase counter
        if nominee_name not in nominee_options:
            
            nominee_options.append(nominee_name)
            
            nominee_votes[nominee_name] = 0
            
        nominee_votes[nominee_name] = nominee_votes[nominee_name] + 1
 #print results and write to text file       
with open(analysis_file,"w") as txt_file:
    
    poll_results = (
        f"\n\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n")
        
        
    print(poll_results)
    
    txt_file.write(poll_results)

#iterate through CSV for vote counts    
    for nominee in nominee_votes:
        
        votes = nominee_votes.get(nominee)
        percentage_of_votes = float(votes) / float(total_votes) * 100
# set conditions and print results        
        if (votes > winner_count):
            winner_count = votes
            winning_nominee = nominee
        voter_result = f"{nominee}: {percentage_of_votes:.3f}% ({votes})\n"
        print(voter_result)
        
        txt_file.write(voter_result)
 #Print Results and Write to txt file       
    Poll_Summary = (
        f"--------------------\n"
        f"Winner: {winning_nominee}\n"
        f"----------------------\n")
    print(Poll_Summary)
    
    txt_file.write(Poll_Summary)