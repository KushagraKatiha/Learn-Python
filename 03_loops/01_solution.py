numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0

for num in numbers:
    if num > 0:
        count += 1
    
final_count = "Total number of positive numbers is: {}"

print(final_count.format(count))