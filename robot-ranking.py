# Ask the user for the number of teams and initialize an empty list
num_teams = int(input("Enter the number of teams: "))
teams = []

# Loop through the number of teams and ask for each team's name and Robot Rank Score
for i in range(num_teams):
    team_name = input(f"Enter the name of team {i+1}: ")
    rrs = int(input(f"Enter {team_name}'s RRS: "))

    # Append the team name and RRS as a tuple to the list of teams
    teams.append((team_name, rrs))

# Write the teams list to a file named robo.txt
with open("robo.txt", "w") as f:
    for team in teams:
        f.write(f"{team[0]},{team[1]}\n")

# Read the contents of robo.txt into a list of tuples
with open("robo.txt", "r") as f:
    teams = [tuple(line.strip().split(",")) for line in f]

# Print the list of teams and their RRS values
print("\nRobo Rank Scores")
print("-----------------")
for team in teams:
    print(f"{team[0]}: {team[1]}")
