import re

# Get the filename from the user
filename = input("Enter the filename: ")

# Write sample text to the file
with open(filename, "w") as obj:
    obj.write("hi this fil contains three four and five length string words !")

# Get the number of lengths to filter
n = int(input("Enter the number of elements in lengths: "))
lengths = []

# Get each word length to filter
for i in range(n):
    num = int(input(f"Enter length {i+1}: "))
    lengths.append(num)

# Read from the file and find words matching the given lengths
with open(filename, 'r') as file:
    words = re.findall(r'\b[a-zA-Z]+\b', file.read())

# Filter and display words for each specified length
for length in lengths:
    filtered_words = [word for word in words if len(word) == length]
    print(f'Words of length {length}:', filtered_words)
