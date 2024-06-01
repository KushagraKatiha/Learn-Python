num = 10

def even_generator(num):
    for i in range(2, num+1, 2):
        yield i

for num in even_generator(num):
    print(num)