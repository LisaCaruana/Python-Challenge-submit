import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

# Split the data on commas, skip the header, hold the first row to calculate avg change
# Set variables to use in calculations 
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)
  first_row =next(csvreader)
  x = int(first_row[1])
  y = 0
  z = 0


# Loop through the data
# Set empty lists for variables, set net profit as float and not string

  total_months = []
  profit_loss = []
  net_profit = float
  net_loss = []
  pl_change = []
  pl_change_avg = []
  greatest_increase = []
  greatest_decrease = []
  average_change = []
  profit_loss.append(int(first_row[1]))

# Iterate through rows in file using csvreader
  for row in csvreader:
# calculate total number of months
    total_months.append(row[0])

# Set Profit/Loss list content
    profit_loss.append(int(row[1]))

# Calculate min and max, formula for calculating monthly change
    change=(int(row[1])-x)
    pl_change.append(change)
  
    if change > y: 
      y = change
      max_month = row[0] 

    if change < z:
      z = change
      min_month = row[0]
        
    x = (int(row[1]))
 
# Sum total net profit
  net_profit=sum(profit_loss)

# Calculate average monthly change from pl_change.append
pl_change_avg = (sum(pl_change)/len(pl_change))

# Pull out min and max change
greatest_increase = y
greatest_decrease = z 

# Print output to terminal 
print(f"Greatest increase: {max_month} {y}")
print(f"Greatest decrease: {min_month} {z}")
print("Total Months: ", len(total_months)+1)
print(f"Net Profit: {net_profit}")
print(f"Average Change: " "{0:.2f}".format(pl_change_avg))

output_path = os.path.join("analysis")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([f"Greatest increase: {max_month} {y}"])
    csvwriter.writerow([f"Greatest decrease: {min_month} {z}"])
    csvwriter.writerow([f"Total Months:{len(total_months)+1}"])
    csvwriter.writerow([f"Net Profit: {net_profit}"])
    csvwriter.writerow([f"Average Change: " "{0:.2f}".format(pl_change_avg)])
max = str(max_month)
min = str(min_month)
total = str(total_months)
profit = str(net_profit)
change = str(pl_change_avg)
all_lists = zip(max, min, total, profit, change)
print(all_lists)

# output_path=os.path.join('analysis')
# output_file=open(output_path, 'w')
# csvwriter = csv.writer(output_file)
# # ls
# csvwriter.writerow(f"Greatest increase: {max_month} {y}")