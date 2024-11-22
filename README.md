# Text File Search Tool

A simple Python utility that allows users to search through text files for specific words or lines. The tool provides two main functionalities: searching for complete lines containing a word and searching for exact word matches.

## Features

- Search for lines containing a specific word (case-insensitive)
- Search for exact word matches (case-insensitive)
- Display number of matches found
- Interactive command-line interface

## Requirements

- Python 3.13
- Text files to search through (.txt format)
⚠️⚠️⚠️txt file must be in the same file directory as the python script⚠️⚠️⚠️


## Usage

Run the script using Python:

```bash
python main.py
```

### Menu Options

1. Search for a line: Finds all lines containing the specified word
2. Search for a word: Finds exact word matches in the text

### Search Modes

#### Line Search
- Searches for lines containing the specified word
- Returns the entire line where the word is found
- Shows the total number of lines containing the word
- Case-insensitive search
- Shows the total count of words found

#### Word Search
- Searches for exact word matches
- Returns all instances of the exact word
- Shows the total count of words
- Case-insensitive search

### Example Usage

```python
# Example for line search
What file do you want to search in? (must be txt) test
Enter a word to search for: pepe
 ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
The word was found in 2 lines
Line: pepe was a war hero (Line 4)
Line: pepe popo kokoko doko was coco (Line 8)
 ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# Example for word search
What file do you want to search in? (must be txt): test
Enter a word to search for: pepe
 ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
The word was found 2 times
Word: pepe (Line 4)
Word: pepe (Line 8)
 ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
```



## Error Handling

The tool includes basic error handling for:
- File not found scenarios
- Empty search results

## Limitations

- Only works with .txt files
- Requires exact file name input (without without file format in the name)



## Author

ByteOfWaffle (Jeremy)


