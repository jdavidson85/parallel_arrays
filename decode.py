alpha = [' ', ',', '!', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i',
         'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T',
         't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

code = ['!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', ')', '0', '_',
        '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', ',', '?', '/', '~', '`', 'a', 's', 'd', 'f', 'g',
        'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'q', 'w']

print('This program will decode a coded text file.')

input_file = input('What is the name of the file to decode? ')

try:
    fileobject = open(input_file, 'r')
    lines = fileobject.readlines()
    fileobject.close()
    coded_message = []

    for letter in lines:
        coded_message.append(letter.strip('\n'))

        decoded_message = []

    for letter in coded_message:
        position = code.index(letter)
        message = str(alpha[position])
        decoded_message.append(message)

    print(''.join(decoded_message))

except:
    print("Error: File doesn't exist!")
