ipl_teams = ["rcb", "rr", "csk", "mi"]

print(ipl_teams[0 : 2])

# ipl_teams[1:2] = "kkr"
# print(ipl_teams)

ipl_teams[1:2] = ["kkr"]
print(ipl_teams)

ipl_teams[1:1] = ["srh", "gt"]
print(ipl_teams)

ipl_teams[1 : 3] = []
print(ipl_teams)

for team in ipl_teams:
    print(team)

for team in ipl_teams:
    print(team, end="-")

print()
if 'kkr' in ipl_teams:
    print("I have kkr")

ipl_teams.pop()
print(ipl_teams)

ipl_teams.remove("rcb")
print(ipl_teams)

ipl_teams.insert(2, 'rcb')
print(ipl_teams)

ipl_teams_new = ipl_teams.copy()
ipl_teams_new.append("srh")

print(ipl_teams_new)
print(ipl_teams)

# list comprehension
two_times_nums = [x * 2 for x in range(10)]
print(two_times_nums)

square_nums = [x**2 for x in range(10)]
print(square_nums)