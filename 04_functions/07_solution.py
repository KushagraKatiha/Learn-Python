def sum_all(*args):
    print(args)
    return sum(args)
    

print(sum_all(2, 3))
print(sum_all(2, 3, 5, 2))
print(sum_all(2, 3, 3, 2, 1, 3))