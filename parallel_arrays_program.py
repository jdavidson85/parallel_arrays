alpha = ['H', 'e', 'l', 'o', 'D', 'y', ',', ' ', '!']
code = ['R', 'j', 'v', 'F', 'x', 'V', 'f', 'a', 'k']

encoded = []

text = input("Enter a phrase to encode:")

for x in text:
    encoded.append(code[alpha.index(x)])

print(encoded)

f = open("encoded.txt", "w")
for x in encoded:
    f.write(x+"\n")
f.close()
