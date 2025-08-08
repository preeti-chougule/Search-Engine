Mini Search Engine

This project implements a simplified search engine using a Trie data structure, tailored for indexing and searching academic HTML files related to Computer Science topics such as Operating Systems, Data Structures, Cybersecurity, and more.

It reads a list of HTML file names from input.txt, parses and indexes their content while ignoring HTML tags, and allows users to search for specific keywords. Results—including file names and word counts—are written to output.txt.

⸻

📁 Files Included
	•	preeti.py: Python script implementing the Mini Search Engine.
	•	input.txt: List of HTML files to process.
	•	output.txt: Output file showing the word search results.
	•	HTML course files:
	•	Operating Systems.html
	•	Data Structures.html
	•	Cybersecurity.html
	•	Computer Networks.html
	•	Introduction.html

⸻

🚀 Features
	•	Trie-based Indexing: Efficient word lookup using a Trie data structure.
	•	Case Insensitive: All words are normalized to lowercase.
	•	HTML Tag Ignoring: Skips content within < > tags.
	•	Stop Word Filtering: Ignores common words like “the”, “is”, “on”, etc.
	•	File-based Word Tracking: Maintains frequency count per word per file.
	•	Search Functionality: User can input space-separated words and get results showing in which files the words appear and how many times.

⸻

🔧 How It Works
	1.	Input Files: Reads HTML file names from input.txt.
	2.	Parsing & Cleaning: Removes HTML tags and non-alphabetical characters.
	3.	Indexing: Inserts each word into a Trie, tracking occurrences by file.
	4.	Search: User enters words, and matching results are written to output.txt.

⸻
📥 Sample input.txt
Operating Systems.html
Data Structures.html
Cybersecurity.html
Introduction.html
Computer Networks.html


📤 Sample output.txt
network appears in the following pages:
    Computer Networks.html: 3 times
    Cybersecurity.html: 2 times

data appears in the following pages:
    Data Structures.html: 4 times
    Introduction.html: 2 times

@ was not found in any file.

▶️ How to Run
	1.	Place all the HTML files in the project directory.
	2.	List their names in input.txt, one per line.
	3.	Run the script: python preeti.py
  4.	Enter search terms when prompted.
	5.	View search results in output.txt.

⸻

🛠️ Requirements
	•	Python 3.x

⸻

🚧 Future Enhancements
	•	Support phrase and Boolean search.
	•	Integrate a GUI or web interface.
	•	Extend support to other file formats (e.g., PDF, DOCX).
	•	Enhance HTML tag parsing with regular expressions.
	•	Improve stop word list customization.

⸻

👩‍💻 Author

Developed by Preeti as part of a practical learning project on data structures and search algorithms.
