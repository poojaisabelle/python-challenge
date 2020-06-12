# Import modules 
import os
import csv 

# Set the path to input the budget_data.csv
election_data = os.path.join("Resources", "election_data.csv")

# Set candidate count to 0 
candidate_votes = [0,0,0,0]
win_percent = [0,0,0,0]


# Open input csv and read 
with open(election_data, "r", encoding="utf-8") as input_csv_file:
    csvreader = csv.reader(input_csv_file, delimiter = ",")
    # Skip the header row 
    csv_header = next(csvreader)

    # List for storing the columns to facilitate calculations
    data_voter_id = list()
    data_county = list()
    data_candidate = list()
    candidate_names = list() 
    winner = list()

    # Use for loop to read through rows and add the data to the newly defined lists 
    for row in csvreader:
        data_voter_id.append(int(row[0]))
        data_county.append(row[1])
        data_candidate.append(row[2])

    # 1. Calculate the total number of votes cast 
    total_votes = len(data_voter_id)
    
    # Use for loop to iterate through row 2 specifically (candidate row)
    for row in data_candidate:

        # 2. Add all candidate names in row to the candidate_name list
        if row not in candidate_names:
            candidate_names.append(row)
        
        # 3. Calculate the total number of votes each candidate received 
        if row == candidate_names[0]:
            candidate_votes[0] += 1

        elif row == candidate_names[1]:
            candidate_votes[1] += 1
        
        elif row == candidate_names[2]:
            candidate_votes[2] += 1 

        elif row == candidate_names[3]:
            candidate_votes[3] += 1 
    
    # 4. Calculate the percentage of votes each candidate won 
    win_percent[0] = ((candidate_votes[0] / total_votes) * 100)
    win_percent[1] = ((candidate_votes[1] / total_votes) * 100)
    win_percent[2] = ((candidate_votes[2] / total_votes) * 100)
    win_percent[3] = ((candidate_votes[3] / total_votes) * 100)

    # Idenfity the highest percentage of votes to identify the winner 
    highest_vote_percentage = max(win_percent[0],win_percent[1],win_percent[2], win_percent[3])

    # 5. Identify the winner of the election based on popular vote 
    if win_percent[0] == highest_vote_percentage:
        winner = candidate_names[0]
    elif win_percent[1] == highest_vote_percentage:
        winner = candidate_names[1]
    elif win_percent[2] == highest_vote_percentage:
        winner = candidate_names[2]
    elif win_percent[3] == highest_vote_percentage:
        winner = candidate_names[3]
    
# Print Election Results 
print("Election Results")
print("--------------------------------------")
print(f"Total Votes: {total_votes} ")
print("--------------------------------------")
print(f"{candidate_names[0]}: {win_percent[0]: .4f}% ({candidate_votes[0]}) ")
print(f"{candidate_names[1]}: {win_percent[1]: .4f}% ({candidate_votes[1]}) ")  
print(f"{candidate_names[2]}: {win_percent[2]: .4f}% ({candidate_votes[2]}) ")       
print(f"{candidate_names[3]}: {win_percent[3]: .4f}% ({candidate_votes[3]}) ")
print("--------------------------------------")
print(f"Winner: {winner} ") 
print("--------------------------------------")   

# Export election results to a new text file 
results_path = "Analysis/election_results.txt"

with open(results_path, 'w') as f:
    f.write("Election Results" + "\n")
    f.write("--------------------------------------" + "\n")
    f.write(f"Total Votes: {total_votes} " + "\n")
    f.write("--------------------------------------" + "\n")
    f.write(f"{candidate_names[0]}: {win_percent[0]: .4f}% ({candidate_votes[0]}) " + "\n")
    f.write(f"{candidate_names[1]}: {win_percent[1]: .4f}% ({candidate_votes[1]}) " + "\n")
    f.write(f"{candidate_names[2]}: {win_percent[2]: .4f}% ({candidate_votes[2]}) " + "\n")
    f.write(f"{candidate_names[3]}: {win_percent[3]: .4f}% ({candidate_votes[3]}) " + "\n")
    f.write("--------------------------------------" + "\n")
    f.write(f"Winner: {winner} " + "\n")
    f.write("--------------------------------------" + "\n")

  

    




    


