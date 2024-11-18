r = open("test.txt")
search = input("Enter a word to search for: ")

for line in r: # Loop through each line in the file
    if search in line: #If the inputted word (in search) is in the line print the line
        print(line)
        list = [line]
        splitlist = line.split() #Splits every word in the line into a list item.
        print(splitlist)
