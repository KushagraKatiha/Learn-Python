# tuples are immutable, list are mutable
ipl_teams = ("rcb", "csk", "mi", "kkr")

# ipl_teams[0] = 'srk'          # will give error

more_teams = ("srh", "rr", "gt")

all_teams = ipl_teams + more_teams
print(all_teams)

if "rcb" in all_teams:
    print("I have rcb")

more_teams = ("srh", "srh", "rr", "gt")
print(more_teams.count("srh"))

(team1, team2, team3, team4) = ipl_teams
print(team1)

print(type(ipl_teams))