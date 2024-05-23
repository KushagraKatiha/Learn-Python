items = ["apple", "banana", "orange", "apple", "mango"]

# for i in range(len(items)):
#     if items.count(items[i]) > 1:
#         print("Duplicate item is: ", items[i])
#         exit()

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate Item is: ", item)
        break
    else:
        unique_item.add(item)