import os
def searchline():
    chosenfile = input("What file do you want to search in? (must be txt) ") #Choose a file to search in.
    r = open(chosenfile + ".txt")
    search = input("Enter a word to search for: ")
    
    found_lines = []  # List to store lines containing the word
    location = 0
    for line in r: # Loop through each line in the file, each loop adds a line to the "line" variable
        location += 1 #Counts the number of lines in the file.
        if search.lower() in line.lower(): #If the word inputted in search is in the line then it wil be added to the list below. .lower makes it case insensitive.
            found_lines.append((line.strip(), location)) #Lines get added to the "found_lines" list and then stripped to remove the whitespace. The location is added to the list as well.
            
    r.close() #Closes file
    
    # Print results
    if found_lines:
        for line in found_lines:  # Loop through all found lines
            return found_lines  #returns line, and sends it to the searchline function in choice.
    else:
        os.system("cls") #Clears screen
        print(f"The word {search} was not found in any lines.")
        input("Press enter to return to menu...")
        os.system("cls") #Clears screen
        return found_lines
        
        

def searchword():
    found_words = []  # List to store found words
    chosenfile = input("What file do you want to search in? (must be txt): ") #Choose a file to search in.
    r = open(chosenfile + ".txt")
    search = input("Enter a word to search for: ")
    location = 0
    for line in r: # Loop through each line in the file, each loop adds a line to the "line" variable
        location += 1 #Counts the number of lines in the file.
        words = line.split()  #Splits every word in the line into a list item and puts it in the words variable. Basically turns the entire text into list items.
        for word in words: #Loops through all the words in the line.
            if search.lower() == word.lower():  #If the inputted search matched the word list item, then add to list with the added below. .lower is used to make it case insensetive.
                found_words.append((word, location)) #Words get added to list with the added location.
    
    r.close() #Closes file
    
    # Print results
    if found_words:
        os.system("cls") #Clears screen
        
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
        for word, location in resultline: 
            print(f"Line: {word} (Line {location})") #Loops through each found word and its location from the results, addong them as word and location variables.
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        input("Press enter to continue...")
        os.system("cls") #Clears screen
        choice()
    else:
        result = searchword()
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        print(f"The word was found {len(result)} times") #Tells if the word was found and how many times it was found. uses "len" to determine number of items.
        for word, location in result: 
            print(f"Word: {word} (Line {location})") #Loops through each found word and its location from the results, addong them as word and location variables.
        print(" ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        input("Press enter to continue...")
        os.system("cls") #Clears screen
        choice()
choice()