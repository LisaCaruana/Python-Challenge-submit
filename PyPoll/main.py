import os
import csv
# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file, skip header
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Set total votes to 0, iterate through rows in CSV reader
    tally = {} 
    totalvotes = 0
    candidate_votes = []
    x = 0
    for row in csvreader:
# Calculates votes for candidate already in tally key
      totalvotes = totalvotes + 1
      vote = row[2]
# Starts tally for new candidate name when found in list
      if vote in tally:
        tally[vote] = tally[vote] + 1
      else:
        tally[vote] = 1

# Prints output to terminal
print("Election Results")
print("*****************")
print(f"Total Votes: {totalvotes}")
print("*****************")

for key in tally.keys():
  percent = (round((tally[key]/totalvotes)*100,3))
  print(f"{key}: {percent}% ({tally[key]})")

print("*****************")

candidate_votes = []
for key in tally.keys(): # The .key is grabbing a list of all the keys w/in that dictionary and then looping through that list. 
  
    candidate_votes.append(tally[key])
  
print(f'{max(tally, key=tally.get)}: {max(candidate_votes)}')

output_path = os.path.join("analysis")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"Total Votes: {totalvotes}"])
    csvwriter.writerow(["*****************"])
    csvwriter.writerow([f"{key}: {percent}% ({tally[key]})"])
    # csvwriter.writerow([f"{key}: {percent}% ({tally[key]})"])
    csvwriter.writerow([f"{max(tally, key=tally.get)}: {max(candidate_votes)}"])
votes = str(totalvotes)
key = str(key)
percent = str(percent)
tally = str(tally)
candidate= str(candidate_votes)
# total = str(total_months)
# profit = str(net_profit)
# change = str(pl_change_avg)
all_lists = zip(votes, key, percent, tally, candidate)
print(all_lists)

        
   # winner = (max(tally[key]))
      # print(max({tally[key]}))

    # winner = max(str(tally[vote]))
  # if {tally[key]}>x
    # winner = max_value({tally[key]})
    # if x > (tally[key])
    # winner = x
    # Create list of tally of individual candidate votes
  
    # candidate_votes = tally[key] #Create list of candidate votes
# dictionary key = candidate value = votes
# Dictionary = { "item" : "value" }
# print(winner)
# winner = max(str(percent))
# winner = max(str(tally[key]))
  # if votes > candidate_votes:
    #     candidate_votes = votes
    #     winner = candidate
    # winner = 

    # print(f"Winner: {winner} ")


# if percent > x:
  # winner = x

# print(winner)
# for key in tally.keys():
  # votes_won = (tally[key])
  
  # if votes_won > x:
    #winner = x

  # percent = (round((tally[key]/totalvotes)*100,3))
 # winner = (votes_won)
  # winner = max({percent})
    

#for tally[key] in tally():
 # winner = max({tally[key]})
  # print(winner)

 # print(f"# Votes cast for {key}: {tally[key]}") 
  # candidate name
  # print(tally[key]) # vote count
 
  # print(f"Percent of Votes for {key}: {percent}%")

  # winner = 


# votes = {tally[key]}
# candidate_votes.append(votes)
# print(max(candidate_votes))
#if votes > x:
 # x = votes
  #winner = max(votes)