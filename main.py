import os
def searchline():
    chosenfile = input("What file do you want to search in? (must be txt) ") #Choose a file to search in.
    r = open(chosenfile + ".txt")
    search = input("Enter a word to search for: ")
    
    found_lines = []  # List to store lines containing the word
    
    for line in r: # Loop through each line in the file, each loop adds a line to the "line" variable
        if search.lower() in line.lower(): #If the word inputted in search is in the line then it wil be added to the list below. .lower makes it case insensitive.
            found_lines.append(line.strip()) #Lines get added to the "found_lines" list and then stripped to remove the whitespace.
            
    r.close() #Closes file
    
    # Print results
    if found_lines:
        for line in found_lines:  # Loop through all found lines
            return found_lines  #returns line
    else:
        os.system("cls") #Clears screen
        print(f"The word {search} was not found in any lines.")
        input("Press enter to return to menu...")
        os.system("cls") #Clears screen
        choice()
        
        

def searchword():
    found_words = []  # List to store found words
    chosenfile = input("What file do you want to search in? (must be txt): ") #Choose a file to search in.
    r = open(chosenfile + ".txt")
    search = input("Enter a word to search for: ")
    
    for line in r: # Loop through each line in the file, each loop adds a line to the "line" variable
        words = line.split()  #Splits every word in the line into a list item and puts it in the words variable. Basically turns the entire text into list items.
        for word in words: #Loops through all the words in the line.
            if search.lower() == word.lower():  #If the inputted search matched the word list item, then add to list with the added below. .lower is used to make it case insensetive.
                found_words.append(word) #Words get added to list
    
    r.close() #Closes file
    
    # Print results
    if found_words:
        os.system("cls") #Clears screen
        print(f"The word {search} was found {len(found_words)} times:") #Tells if the word was found and how many times it was found. uses "len" to determine number of items.
        return found_words
    else:
        print(f"The word '{search}' was not found.")
        return found_words
        
            
            
            
def choice(): #Choose if you want to search for a line or a word.
    print(" ————————————————————————")
    print("|1.   Search for a line  |")
    print("|2.   Search for a word  |")
    print(" ————————————————————————")
    wordorline = input("Do you want to search for a line or a word? ")
    
    if wordorline == "1": 
        resultline = searchline()
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        for line in resultline: #Loops through all lines in the resultline list and adds it to line. This way I can print all the lines that were found as a string.
            print(line) #Prints returned lines.
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        input("Press enter to continue...")
        os.system("cls") #Clears screen
        choice()
    else:
        result = searchword()
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        print(result) #Prints returned list words. Not coverting this to string because I feel it's easier to read them as list items.
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        input("Press enter to continue...")
        os.system("cls") #Clears screen
        choice()
choice()