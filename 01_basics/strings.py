greet = "hello world"
first_char = greet[0]
print(first_char)

slice_greet = greet[0:6]
print(slice_greet)

num_list = '0123456789'
print(num_list[0 : 9 : 2])

print(num_list[0 : 9 : -1])
print(num_list[0 : 9 : -2])
print(num_list[0 : -2])


print(greet.lower())
print(greet.upper())

greet = "       hello world          "
print(greet.strip())

greet = "This is a Namaste"
print(greet.replace("Namaste", "Hello"))

greet = "Hello, Namaste, Hola"
print(greet.split(", "))

greet = "Hello World"
print(greet.find("World"))

greet = "Hello World World World World"
print(greet.count("World"))

greet = "Hello World"
people = 2

greeting = 'I said {} to {} people.'            # order formatting
print(greeting.format(greet, people))

greet_type = ["Hello", "Namaste", "Hola"]
print("-".join(greet_type))

greet = "Hello World"
print(len(greet))


for letter in greet:
    print(letter)

print("World" in greet)











