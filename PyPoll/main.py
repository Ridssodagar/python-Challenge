import csv 

my_report = open("Analysis/Report.txt","w")
data = csv.reader(open("Resources/election_data.csv"))

next(data)

votes = 0
candidates = {}

for row in data:
    votes += 1 

    if row[2] not in candidates.keys():
        candidates[row[2]] = 0
    
    candidates[row[2]] += 1

output = f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
'''

winner = ["",0]

for candidate in candidates.keys():
    canVotes = candidates[candidate]
    output += f"{candidate}: {canVotes/votes*100:.3f}% ({canVotes:,})\n"
    if canVotes > winner[1]:
        winner[0] = candidate
        winner[1]= canVotes

output += f'''-------------------------
Winner: {winner[0]}
-------------------------
'''
print(output)
my_report.write(output)

