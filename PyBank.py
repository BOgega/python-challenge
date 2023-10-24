#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:17:31 2023

@author: bradyogega
"""
#import csv
import csv
#Assingn files to variable
load_file =("/Users/bradyogega/Downloads/Starter_Code 3/PyBank/Resources/budget_data.csv")
csv_analysis = ("/Users/bradyogega/Desktop/PyBank/PyBank_Analysis.txt")

#Assign Variables
Total_Months = 0
Profit_Change = 0
Previous_Profit = 0
Net_Total_Profit = 0
Average_Change = 0.00
Greatest_Increase = ["",0]
Greatest_Decrease = ["",1000000000000]
Month_of_Change = []
Profit_Change_List = []
#Read CSV File & Create Lists   
with open(load_file) as csv_reader :
    reader = csv.DictReader(csv_reader)
    
    #Iterate through CSV and track totals
    for row in reader:
        Total_Months = Total_Months + 1
        Net_Total_Profit = Net_Total_Profit + int(row["Profit/Losses"])
        
        Profit_Change = int(row["Profit/Losses"]) - Previous_Profit
        Previous_Profit = int(row["Profit/Losses"])
        Profit_Change_List = Profit_Change_List + [Profit_Change]
        Month_of_Change = Month_of_Change = [row["Date"]]
        
        
#Set Conditions to Track Greatest Increase & Decrease    
        if (Profit_Change > Greatest_Increase[1]):
            Greatest_Increase[0] = row["Date"]
            Greatest_Increase[1] = Profit_Change
            
        if (Profit_Change < Greatest_Decrease[1]):
            Greatest_Decrease[0] = row["Date"]
            Greatest_Decrease[1] = Profit_Change
            
            
#Calculate Average Change    
    Average_Change = (sum(Profit_Change_List) / len(Profit_Change_List))
    Average_Change = round(Average_Change,2)
    
    
#Format and Print Results    
    Result = (f"\nFinancial Analysis\n"
          f"--------------------------\n"
          f"Total Months: {Total_Months}\n"
          f"Total: ${Net_Total_Profit}\n"
          f"Average Change: ${Average_Change}\n"
          f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
          f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})\n"
          ) 
print(Result)

with open(csv_analysis,"w") as txt_file:
    txt_file.write(Result)