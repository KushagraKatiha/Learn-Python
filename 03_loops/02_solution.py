given_number = 5
positive_sum = 0

for i in range(1, given_number+1):
    if i % 2 == 0:
        positive_sum += i
print("Sum of positive upto", given_number, "is", positive_sum)