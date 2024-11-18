
def searchline():
    r = open("test.txt")
    search = input("Enter a word to search for: ")
    
    found_lines = []  # List to store lines containing the word
    
    for line in r: # Loop through each line in the file
        if search.lower() in line.lower(): #If the word inputted in search is in the line then it wil be added to the list below. .lower makes it case insensitive.
            found_lines.append(line)  # strip() removes the exta empty room between lines, like if someone has pressed enter 20 times there won't be a giant gap.
            
    r.close() #Closes file
    
    # Print results
    if found_lines:
        print(f"The word {search} was found in {len(found_lines)} lines:")
        for line in found_lines:
            print(line)
        foundline = True
    else:
        print(f"The word {search} was not found in any lines.")
        foundline = False
        

def searchword():
    found_words = []  # List to store found words
    
    r = open("test.txt")
    search = input("Enter a word to search for: ")
    
    for line in r: # Loop through each line in the file
        words = line.split()  #Adds the lines checked to "words" and Splits every word in the line into a list item. Basically turns the entire text into list items.
        for word in words: #Loops through all the words 
            if search.lower() == word.lower():  #If the inputted search matched the word list item, then add to list with the added below. .lower is used to make it case insensetive.
                found_words.append(word) #Words get added to list
    
    r.close() #Closes file
    
    # Print results
    if found_words:
        print(f"The word {search} was found {len(found_words)} times:") #Tells if the word was found and how many times it was found. uses "len" t determine number of items.
        print(found_words) #Prints the list
        foundword = True
    else:
        print(f"The word '{search}' was not found.")
        foundword = False
            
wordorline = input("Do you want to search for a line or a word? Write 1 for line and 2 for word ")
if wordorline == "1": 
    searchline()
else:
    searchword()
    