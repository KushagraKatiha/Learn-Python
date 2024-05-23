number = int(input("Enter a number: "))

isPrime = True

if number > 1:
    for i in range(2, number):
        if(number % i) == 0:
            isPrime = False
            break

if isPrime:
    print("Number is prime")
else:
    print("Number is not Prime")