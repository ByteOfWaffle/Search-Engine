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

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/text-file-search-tool.git
cd text-file-search-tool
```

2. No additional dependencies are required as the tool uses only Python standard library.

## Usage

Run the script using Python:

```bash
python search_tool.py
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

#### Word Search
- Searches for exact word matches
- Returns all instances of the exact word
- Shows the total count of word occurrences
- Case-insensitive search

### Example Usage

```python
# Example for line search
Enter a file to search in: sample
Enter a word to search for: hello
The word hello was found in 2 lines:
Hello world, this is a test
Hello there, how are you?

# Example for word search
Enter a file to search in: sample
Enter a word to search for: hello
The word hello was found 3 times:
['Hello', 'Hello', 'hello']
```

## Function Documentation

### `searchline()`
- Prompts for a file name and search term
- Searches for lines containing the specified word
- Returns the matched lines with whitespace stripped
- Case-insensitive search

### `searchword()`
- Prompts for a file name and search term
- Searches for exact word matches
- Returns a list of matched words
- Case-insensitive search

### `choice()`
- Displays the main menu
- Handles user input for search mode selection
- Calls appropriate search function based on user choice

## Error Handling

The tool includes basic error handling for:
- File not found scenarios
- Empty search results

## Limitations

- Only works with .txt files
- Requires exact file name input (without .txt extension)
- Loads entire file into memory



## Author

ByteOfWaffle


