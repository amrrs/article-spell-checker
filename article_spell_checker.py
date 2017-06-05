import newspaper
from nltk import word_tokenize
import enchant
import re
#url = 'https://byrslf.co/a-smile-no-the-smile-e37af3f65b99#.2ccdxl5rp' #No Spelling Mistakes
url = 'https://hackernoon.com/dilemmas-of-a-digital-lifestyle-27c044940157'

# ### Extracting the Article Content

my_article = newspaper.Article(url,language='en')
my_article.download()
my_article.parse()
# ### Printing the parsed Article Text 
print(my_article.text)
# ### Spell-Checking the tokenized words 
d = enchant.Dict("en_US")
non_dict_words = list(set([word.encode('ascii', 'ignore') for word in word_tokenize(my_article.text) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] ))
non_dict_words
