# Import modules 
import os
import csv 

# Set the path to input the budget_data.csv
budget_data = os.path.join("Resources", "budget_data.csv")

# Open input csv and read 
with open(budget_data, "r", encoding="utf-8") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    # Skip the header row 
    csv_header = next(csvreader)
    
    # List for storing the columns to facilitate calculations 
    data_months = list()
    data_profit_loss = list()
    data_average_change = list()

    # Using for loop to read through rows and adding them to the new lists  
    for rows in csvreader:
        data_months.append(rows[0])
        data_profit_loss.append(int(rows[1]))

    # 1. Calculating the total number of months included in the dataset
    total_months = len(data_months)

    # 2. Calculating the net total amount of Profit/Losses over the entire period 
    total_profit_loss = sum(data_profit_loss)


  
    


    




