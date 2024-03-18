#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:


#Setting path for csv file


# In[13]:


# Path to the CSV file
csvpath = os.path.join("/Users/davidspir/Downloads/budget_data.csv")



# In[14]:


# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
months = []



# In[22]:


# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first
    csv_header = next(csvreader)
     # Iterate through the rows of the CSV file
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Sum the total profit/loss
        total_profit_loss += int(row[1])

        # Track the changes in profit/loss
        if total_months > 1:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])

        # Update previous profit/loss
        previous_profit_loss = int(row[1])



# In[23]:


# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)


# In[24]:


# Find the greatest increase and decrease in profit/loss
greatest_increase = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index]

greatest_decrease = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index]


# In[25]:


# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


# In[29]:


# Export the analysis to a text file
output_file = os.path.join("/Users/davidspir/Downloads/budget_data.csv")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")


# In[31]:





# In[ ]:




