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
    header = next(csvreader)

    total_votes = 0
    for row in csvreader:
        candidate = row[2]
        total_votes += 1 

        if candidate not in all_candidates:
            all_candidates.append(candidate)
            candidate_dict[candidate] = 0

        candidate_dict[candidate] += 1

with open("analysis/election_results.txt", "w") as textfile:

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

    print(election_results)
    textfile.write(election_results)

    winner_total = 0
    winner_name = ""

    for candidate in all_candidates:
        votes = candidate_dict[candidate]
        vote_percent =(votes/total_votes) * 100

        if votes > winner_total:
            winner_total = votes
            winner_name = candidate 

        print(f"{candidate}: {vote_percent:.2f}% {votes}\n")
        textfile.write(f"{candidate}: {vote_percent:.2f}% {votes}\n")

    print("------------------------------------\n")
    print("Winner: " + winner_name)
    print("\n------------------------------------")
    textfile.write("------------------------------------\n")
    textfile.write("Winner: " + winner_name)
    textfile.write("\n------------------------------------")








#calculate total votes
#total_votes = len(Voter_id)

#calculate # of votes per candidate
#candidate_1 = len(candidate_1)
#candidate_2 = len(candidate_2)
#candidate_3 = len(candidate_3)

#calculate % of votes won for candidates
#candidate1_percent = (candidate_1 / total_votes) * 100
#candidate1_percent = (candidate_2 / total_votes) * 100
#candidate1_percent = (candidate_3 / total_votes) * 100

#calculate popular vote winner
#winner = max(candidate_1, candidate_2, candidate_3)


#print out results
#print("Election Results")
#print("------------------------------------")
#print("Total Votes: " + str(total_votes))
#print("------------------------------------")
#print(f"{candidate}: {str(candidate_percent)}% {str(candidate_votes)}")
#print(Candidate 1, %, # of votes)
#print(Candidate 2, %, # of votes)
#print(Candidate 3, %, # of votes)
#print("------------------------------------")
#print("Winner: " + popular winner)
#print("------------------------------------")