ipl_trophies = {
    'rcb': 0,
    'csk': 5,
    'kkr': 2,
    'mi': 5
}

print(ipl_trophies['csk'])
print(ipl_trophies.get("kkr"))

print(ipl_trophies.get('cskk'))         # will give None
# print(ipl_trophies['cskkk'])          # will give keyError

ipl_trophies['rcb'] = 'agle sala cup namde'
print(ipl_trophies)

for team in ipl_trophies:
    print(team)

for team in ipl_trophies:
    print(team, ipl_trophies[team])

for key, value in ipl_trophies.items():
    print(key, value)

if 'rcb' in ipl_trophies:
    print("I have rcb")

print(len(ipl_trophies))

# Add new team
ipl_trophies["pbsk"] = 0

print(ipl_trophies)

ipl_trophies.pop("mi")
print(ipl_trophies)

ipl_trophies.popitem()
print(ipl_trophies)

del ipl_trophies['kkr']
print(ipl_trophies)

squared_nums = {
    x:x**2 for x in range(10)
}

print(squared_nums)

squared_nums.clear()
print(squared_nums)

ipl_teams = ['rcb', 'srh', 'mi', 'kkr']
default_rival = 'csk'

rival_set = dict.fromkeys(ipl_teams, default_rival)
print(rival_set)


