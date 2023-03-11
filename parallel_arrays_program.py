def main():
    alpha = [' ', ',', '!', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i',
             'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T',
             't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

    code = ['!', '1', '@', '2', '#', '3', '$', '4', '%', '5', '^', '6', '&', '7', '*', '8', '(', '9', ')', '0', '_',
            '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', ',', '?', '/', '~', '`', 'a', 's', 'd', 'f', 'g',
            'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'q', 'w']

    outline = []

    print("This program will take a sentence and convert it into a secret code and save it to a text file")

    secret = input("Enter message you want put into code: ")

    for letter in secret:
        letter_index = alpha.index(letter)
        code_value = code[letter_index]
        outline.append(code_value)
    print(outline)

    outfile = open("coded.txt", "w")
    for item in outline:
        outfile.write(str(item) + "\n")
    outfile.close()


main()
