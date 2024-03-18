#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:


# Path to the CSV file


# In[11]:


csvpath = os.path.join ("/Users/Shared/election_data.csv")
    
    


# In[12]:


# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0


# In[16]:


# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)

    # Iterate through the rows of the CSV file
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate's name
        candidate = row[2]
        
  # Add candidate to the dictionary if not already present
        if candidate not in candidates:
            candidates[candidate] = 0

        # Increment the candidate's vote count
        candidates[candidate] += 1


# In[17]:


# Find the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes


# In[18]:


# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}


# In[19]:


# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# In[21]:


# Export the analysis to a text file
output_file = os.path.join("/Users/Shared/election_data.csv")
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        txtfile.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")


# In[ ]:




