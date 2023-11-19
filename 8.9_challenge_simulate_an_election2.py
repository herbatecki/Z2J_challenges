import random

def simulate_election(probability_candidateA):
    if random.random() < probability_candidateA:
        return "candidateA"
    else:
        return "candidateB"

simulation_num = 10_000
num_times_A_wins = 0
num_times_B_wins = 0

for trial in range(simulation_num):
    votes_candidateA = 0
    votes_candidateB = 0
    if simulate_election(0.87) == "candidateA":
        votes_candidateA += 1
    else:
        votes_candidateB += 1

    if simulate_election(0.65) == "candidateA":
        votes_candidateA += 1
    else:
        votes_candidateB += 1

    if simulate_election(0.17) == "candidateA":
        votes_candidateA += 1
    else:
        votes_candidateB += 1

    if votes_candidateA > votes_candidateB:
        num_times_A_wins = num_times_A_wins + 1
    else:
        num_times_B_wins = num_times_B_wins + 1

        
percent_candidateA = num_times_A_wins / simulation_num
print(f"Percentage of times in which Candidate A wins equal {percent_candidateA:.2%}")

