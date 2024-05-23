given_number = 4

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(given_number, "x", i, "=", given_number*i)
