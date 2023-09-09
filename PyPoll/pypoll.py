import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('C:/Users/ormon/OneDrive/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

#create lists
all_candidates = []
candidate_dict = {}

# Read the csv file & split data on ,:
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    header = next(csvreader)

    #begin counting rows to calculate total votes
    total_votes = 0

    #start looping through csv file to put candidate names into list & tally total votes
    for row in csvreader:
        candidate = row[2]
        total_votes += 1 

        #check to see if the candidate name just picked up is in the dictionary of all candidates
        #if the name is not in the dictionary, then add the name & begin counting the votes for that candidate
        if candidate not in all_candidates:
            all_candidates.append(candidate)
            candidate_dict[candidate] = 0

        #increase the candidate vote counter by 1
        candidate_dict[candidate] += 1

#set output folder
with open("C:/Users/ormon/OneDrive/Desktop/python-challenge/PyPoll/analysis/PyPoll_results.txt", "w") as textfile:

    #create a function to print output header & total vote calcucation
    election_results = (
        f"Election Results"
        f"\n"
        f"\n"
        f"-------------------------"
        f"\n"
        f"\n"
        f"Total Votes: {total_votes}"
        f"\n"
        f"\n"
        f"-------------------------"
        f"\n")

    #print election results to terminal
    print(election_results)

    #print election results to txt file
    textfile.write(election_results)
    textfile.write("\n")

    #start calculating total votes of winner
    winner_total = 0

    #set the variable of the winner's name to accept a string
    winner_name = ""

    #loop through the names in the all_candidates list
    for candidate in all_candidates:

        #pull the total votes for each candidate    
        votes = candidate_dict[candidate]

        #calculate the % of votes the candidate received
        vote_percent =(votes/total_votes) * 100

        #check to see if current candidate is the winner & if true, then make current candidate the winner & their votes the winning votes
        if votes > winner_total:
            winner_total = votes
            winner_name = candidate 

        #print current candidate, % of votes & count of votes to terminal
        print(f"{candidate}: {vote_percent:.3f}% ({votes})")
        print("\n")

        #print current candidate, % of votes & count of votes to text file
        textfile.write(f"{candidate}: {vote_percent:.3f}% ({votes})")
        textfile.write("\n")
        textfile.write("\n")

    #print the winner's name to the terminal
    print("------------------------------------")
    print("\n")
    print("Winner: " + winner_name)
    print("\n")
    print("------------------------------------")

    #print the winner's name to the text file
    textfile.write("------------------------------------")
    textfile.write("\n")
    textfile.write("\n")   
    textfile.write("Winner: " + winner_name)
    textfile.write("\n")
    textfile.write("\n")
    textfile.write("------------------------------------")