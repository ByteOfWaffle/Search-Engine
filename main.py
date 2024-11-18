
def searchline():
    r = open("test.txt")
    search = input("Enter a word to search for: ")

    for line in r: # Loop through each line in the file
        if search in line: #If the inputted word (in search) is in the line print the line
            print(line)
            list = [line]
            splitlist = line.split() #Splits every word in the line into a list item.
            print(splitlist)
            foundline = True
        else:
            foundline = False
        

def searchword():
    r_ord = open("test.txt")
    search = input("Enter a word to search for: ")

    for line in r: # Loop through each line in the file
        if search in line: #If the inputted word (in search) is in the line print the line
            print(search)
            foundword = True
        else:
            foundword = False
            
wordorline = input("Do you want to search for a line or a word? Write 1 for line and 2 for word ")
if wordorline == "1": 
    searchline()
else:
    searchword()
    

