# Import csv reader
import csv
import os
# Import the files
Pypoll_data = os.path.join("election_data.csv")
analysis_txt = os.path.join("analysis.txt")
# Set the counters and dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}
winner = ""
winner_count = 0
# Open csv file and convert into keys and values
with open(Pypoll_data) as election_data:
    reader = csv.reader(election_data)
# Add loop for reader
    header = next(reader)
    for row in reader:
# Add the total vote count
        total_votes = total_votes + 1
# Get the name of the candidate
        candidate_name = row[2]
# Add conditions to candidates if the candaidate doesn't match
        if candidate_name not in candidate_options:
# Add to the list of the candidates in the running
            candidate_options.append(candidate_name)
# Add to tracking voter count
            candidate_votes[candidate_name] = 0
# Then add a vote for that candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
#Print the results and export the data to the text file
    with open(analysis_txt, "w") as txt_file:
        election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)
# Set loop to count to determine the winner
        for candidate in candidate_votes:
            #Retrieve the vote count and percentage
            votes = candidate_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
    # Determine the highest amount of votes and winning candidate
            if (votes > winner_count):
                winner_count = votes
                winning_candidate = candidate
    # Print each candidates vote amount and percentage
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            print(voter_output)

            txt_file.write(voter_output)
    #Print the winning candidate
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"--------------------------\n"
        )
        print(winning_candidate_summary)
    # Save the winners name to the text file
        txt_file.write(winning_candidate_summary)


