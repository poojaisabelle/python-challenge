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
    profit_loss_change = list()

    # Use for loop to read through rows and add the data to the newly defined lists  
    for rows in csvreader:
        data_months.append(rows[0])
        data_profit_loss.append(int(rows[1]))

    # 1. Calculate the total number of months included in the dataset
    total_months = len(data_months)

    # 2. Calculate the net total amount of Profit/Losses over the entire period 
    total_profit_loss = sum(data_profit_loss)

    # Subtract every subsequent value with the value before it to determine each change that occurs month-to-month
    for x in range(1, len(data_profit_loss)):
         profit_loss_change.append((int(data_profit_loss[x]) - int(data_profit_loss[x-1])))

    # 3. Calculate the average of the changes in "Profit/Losses" over the entire period
    average_change = sum(profit_loss_change) / len(profit_loss_change) 

    # 4. Calculate the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profit_loss_change)

    # Obtain the date associated with greatest increase 
    date_greatest_increase = data_months[profit_loss_change.index(greatest_increase)+1]
   
    # 5. Calculate greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profit_loss_change)

    # Obtain date associated with greatest decrease
    date_greatest_decrease = data_months[profit_loss_change.index(greatest_decrease)+1]


    # Print all financial results 
    print("Financial Analysis")
    print("--------------------------------------------------")
    print(f"Total Months: {total_months} ")
    print(f"Net Total Profit/Loss: ${total_profit_loss}")
    print(f"Average Change in Profit/Loss: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {date_greatest_increase} ${greatest_increase} ")
    print(f"Greatest Decrease in Profits: {date_greatest_decrease} ${greatest_decrease} ")

# Export results to a new text file 
analysis_path = "Analysis/financial_results.txt"

with open(analysis_path, 'w') as f:
    f.write("Financial Analysis" + "\n")
    f.write("--------------------------------------------------" + "\n")
    f.write(f"Total Months: {total_months} " + "\n")
    f.write(f"Net Total Profit/Loss: ${total_profit_loss}" + "\n")
    f.write(f"Average Change in Profit/Loss: ${average_change:.2f}" + "\n")
    f.write(f"Greatest Increase in Profits: {date_greatest_increase} ${greatest_increase} " + "\n")
    f.write(f"Greatest Decrease in Profits: {date_greatest_decrease} ${greatest_decrease} " + "\n")

    



  





  
    


    




