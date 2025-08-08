#preethi chougule
# Node class for Trie structure: Represents an individual node in the Trie.
class Node:
    def __init__(self):
        self.children = [None] * 26  # An array to hold the child nodes for each letter in the alphabet.
        self.endOfWord = False  # A flag to mark if the node is the end of a word.
        self.pageContains = set()  # A set to store the unique files that contain the word.
        self.count = {}  # A dictionary to map file names to the frequency of the word in those files.

# Trie class: Implements the Trie data structure for efficient word management and search.
class Trie:
    def __init__(self):
        self.root = self.getNode()  # Initializes the Trie with a root node.

    def getNode(self):
        return Node()  # A helper method to generate a new Trie node.

    def insert(self, key, file):
        key = key.lower()  # Convert the word to lowercase for case-insensitive insertion.
        file = file.strip()  # Remove leading/trailing spaces from the file name.
        if not key.strip():  # Skip empty or whitespace-only words.
            return
        stop_words = set(['a', 'an', 'the', 'above', 'across', 'against', 'along',
                          'among', 'around', 'at', 'before', 'behind', 'below', 'beneath',
                          'beside', 'between', 'by', 'down', 'from', 'in', 'into', 'near', 'of',
                          'off', 'on', 'to', 'toward', 'under', 'upon', 'with', 'within',
                          'i', 'he', 'him', 'you', 'we', 'him', 'her', 'yours', 'theirs', 'someone',
                          'where', 'when', 'yourselves', 'themselves', 'oneself', 'is', 'hers', 'when',
                          'whom', 'whose', 'each other', 'one', 'everyone', 'nobody', 'none',
                          'each', 'anywhere', 'anyone', 'nothing'])
        if key in stop_words:  # Skip insertion if the word is in the list of stop words.
            return
        curNode = self.root
        for char in key:
            if 'a' <= char <= 'z':  # Ensure that the character is a lowercase letter.
                index = ord(char) - ord('a')  # Calculate the index for the current character.
                if not curNode.children[index]:  # If the node doesn't exist, create it.
                    curNode.children[index] = self.getNode()
                curNode = curNode.children[index]
        curNode.endOfWord = True  # Mark the node as the end of the word.
        curNode.pageContains.add(file)  # Add the file to the set of files containing the word.
        curNode.count[file] = curNode.count.get(file, 0) + 1  # Update the word count in the file.

    def search(self, key):
        curNode = self.root
        for char in key:
            if 'a' <= char <= 'z':  # Ensure the character is a lowercase letter.
                index = ord(char) - ord('a')  # Find the index corresponding to the character.
                if not curNode.children[index]:  # If no node exists for the character, return False.
                    return False, [], {}
                curNode = curNode.children[index]
            else:
                return False, [], {}  # Return False for non-alphabetical characters.
        return curNode.endOfWord, curNode.pageContains, curNode.count

# Main execution
t = Trie()
try:
    with open('input.txt', 'r') as fi:
        files = fi.readlines()  # Read the list of files from the input file.
    if not files:  # Check if no files are listed.
        raise FileNotFoundError  # Raise an exception if the list is empty.
except FileNotFoundError:
    print("Files not found.")
    exit()

for file in files:
    try:
        with open(file.strip(), 'r') as fr:
            text = fr.read()  # Read the entire content of the current file.
    except FileNotFoundError:
        print(f"File {file.strip()} not found.")
        continue
    inside_tag = False
    word = ""
    for ch in text:
        if inside_tag and ch == '>':  # Handle HTML-like tags or brackets.
            inside_tag = False
            word = ""
        elif inside_tag:
            continue
        elif ch == '<':  # Start of an HTML tag or similar element.
            inside_tag = True
            if word:
                t.insert(word, file)  # Insert the word before the tag.
            word = ""
        elif ch.isalpha():  # If the character is a letter, continue forming the word.
            word += ch
        else:  # When a non-alphabet character is encountered, insert the current word and reset.
            if word:
                t.insert(word, file) 
            word = ""

with open('output.txt', 'w') as fo:
    search_query = input('Enter Search Query: ').strip()  # Take user input for the search query.
    if not search_query:  # Ensure the input is not empty.
        print("Please enter a valid search query.")
        exit()
    words = search_query.split()  # Split the query into individual words.
    search_results = {}
    for word in words:
        found, pages, counts = t.search(word.lower())  # Search for each word in the Trie.
        search_results[word] = (found, pages, counts)

    all_found = True
    for word, (found, pages, counts) in search_results.items():
        if found:
            fo.write(f'{word} appears in the following files:\n')
            for page in pages:
                fo.write(f'    {page.strip()}: {counts[page]} occurrences\n')
            fo.write('\n')
        else:
            all_found = False
            fo.write(f'{word} was not found in any file.\n\n')

    if not all_found:
        fo.write("Some search terms were not found in any file.")
