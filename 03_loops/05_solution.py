myStr = "array"

for i in range(len(myStr)):
    if myStr.count(myStr[i]) == 1:
        print(myStr[i])
        break

