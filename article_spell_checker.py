import newspaper
from nltk import word_tokenize
import enchant
import re
url = 'https://hackernoon.com/dilemmas-of-a-digital-lifestyle-27c044940157' #input URL
my_article = newspaper.Article(url,language='en') # ### Extracting the Article Content
my_article.download()
my_article.parse()  
d = enchant.Dict("en_US") # ### Spell-Checking the tokenized words 
print(list(set([word.encode('ascii', 'ignore') for word in word_tokenize(my_article.text) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] )))

