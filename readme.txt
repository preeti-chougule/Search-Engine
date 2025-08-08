# README

## Trie-based Search Engine for Text Files

This project implements a simplified search engine using a Trie data structure. The search engine processes a set of text files, indexes their content, and allows users to search for specific words. The program identifies the files where the words appear and counts their occurrences.

---

### Features
- **Efficient Word Indexing:** Uses a Trie data structure for quick word lookups.
- **Case Insensitivity:** Normalizes all words to lowercase for consistent indexing and searching.
- **Exclusion of Common Words:** Ignores a predefined list of stop words (e.g., "a," "the," "on").
- **HTML Tag Handling:** Skips content inside angle brackets (`< >`) to exclude HTML-like tags.
- **Word Occurrence Count:** Tracks the number of times each word appears in each file.
- **File-wise Results:** Outputs search results organized by file.

---

### How It Works

1. Input Files:
   - The program reads a list of file names from `input.txt`.
   - Each file is opened, read, and processed to extract words.

2. Word Processing:
   - Words are extracted by skipping non-alphabetical characters.
   - Words inside angle brackets (`< >`) are ignored to handle HTML tags.

3. Indexing:
   - Words are stored in a Trie, with each node representing a character.
   - Each word node tracks:
     - Files containing the word.
     - Count of the word's occurrences in each file.

4.Search:
   - Users input words to search.
   - The program checks for their presence in the Trie.
   - Outputs the results to `output.txt`, including:
     - Files where the words appear.
     - Count of occurrences in each file.

---

### File Details

- `input.txt`:** Contains the list of file names to be processed. Each file name should be on a new line.
- `output.txt`:** Stores the search results, listing files and word counts for each query.
- `Trie` and `Node` classes:** Implement the core Trie functionality.

---

### How to Run

1. Place the file names you want to process in `input.txt`.
2. Run the script:
   ```bash
   python script.py
   ```
3. Enter the search terms when prompted.
4. Check `output.txt` for the results.

---

### Example

`input.txt`
```
file1.txt
file2.txt
```

Search Input
```
example word
```

`output.txt`
```
example appears in the following pages:
    file1.txt: 2 times
    file2.txt: 1 times

word appears in the following pages:
    file1.txt: 3 times

Some words were not found in any file.
```

---

### Error Handling

- **Missing Files:** If a file listed in `input.txt` is missing, the program skips it and displays an error message.
- **Empty Input:** The program alerts the user if no input is provided during the search.

---

### Requirements

- Python 3.x

---

### Improvements and Future Work

- Add support for more complex queries (e.g., phrase searching).
- Optimize memory usage for larger datasets.
- Enhance stop word list and provide customization options.
- Integrate a user-friendly interface or web application.

---

### Author

This project was developed as part of a learning exercise on data structures and search algorithms.