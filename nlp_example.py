# Natural Language Processing Example From Datacamp

# Importing requests, BeautifulSoup, nltk, and Counter
import requests
from bs4 import BeautifulSoup
import nltk
from collections import Counter

# Getting the Moby Dick HTML 
r = requests.get("https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm")

# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Printing the first 2000 characters in html
html[200]

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html)

# Getting the text out of the soup
text = soup.text

# Printing out text between characters 32000 and 34000
print(text[32000:34000])


# Creating a tokenizer
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("\w+")

# Tokenizing the text
tokens = tokenizer.tokenize(text)

# Printing out the first 8 words / tokens 
print(tokens[:8])

# Create a list called words containing all tokens transformed to lower-case
words =[t.lower() for t in tokens]

# Printing out the first 8 words / tokens 
print(words[:8])


# Create a list words_ns containing all words that are in words but not in sw
words_ns = [w for w in words if w not in sw]

# Printing the first 5 words_ns to check that stop words are gone
print(words_ns[:5])

# Initialize a Counter object from our processed list of words
count = Counter(words_ns)

# Store 10 most common words and their counts as top_ten
top_ten = count.most_common(10)

# Print the top ten words and their counts
print(top_ten)

# What's the most common word in Moby Dick?
most_common_word = 'whale'