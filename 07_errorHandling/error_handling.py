# file = open('./07_errorHandling/youtube.txt', 'w')

# try:
#     file.write('I wrote this file')
# finally:
#     file.close()

with open('./07_errorHandling/youtube.txt', 'w') as file:
    file.write('I wrote this file')