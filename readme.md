
## Article Spell-Checking with Newspaper (The wonderful article summarization PyLib)

### Importing Newspaper for article extraction, PyEnchant for Spell Checking, re & nltk for text operations


```python
import newspaper
from nltk import word_tokenize
import enchant
import re
```


```python
#url = 'https://byrslf.co/a-smile-no-the-smile-e37af3f65b99#.2ccdxl5rp' #No Spelling Mistakes
url = 'https://hackernoon.com/dilemmas-of-a-digital-lifestyle-27c044940157'
```

### Extracting the Article Content


```python
my_article = newspaper.Article(url,language='en')
my_article.download()
my_article.parse()
```

### Printing the parsed Article Text 


```python
print(my_article.text)
```

    Dilemmas of a Digital Lifestyle
    
    Is two blueteeth one bluetooth too many?
    
    A few weeks ago, I finally traded in my old car for a newer model. Among other things, the new car came with a decent audio system that had four speakers, and bluetooth connectivity.
    
    After a bit of fiddling, I was able to connect my phone via Bluetooth to the car’s system. I was late to the party, but it was still quite a thrill to take handsfree calls while driving, and enjoy the luxury of listening to the caller’s voice over the car’s stereo system. However the Bluetooth only connects to one device at a time. And that can be an issue if you have kids at home.
    
    My 14 year old and all her friends have their own personal collections of songs on their phones or iPods. And they are all dying to try out their songs on the car’s music system every time I cart them around.
    
    I didn’t want them using the car’s Bluetooth as that would mean losing my handsfree calls, and going through the whole circus of disconnecting and reconnecting my phone. The car does have USB and auxiliary ports but the first can’t connect to the phones, and the second needs a cable that has to be extra long to reach the kids in the back seat, which can be kind of messy.
    
    My solution was a little Bluetooth adapter that I picked up on eBay for around ₹300 ($5). One end has a USB connector, and the other an auxiliary cable. You power it by plugging it in to the car’s USB port. You then pair the bluetooth adapter with the phone, after which it pipes music played on the phone into car’s audio system, via the car’s auxiliary port. It’s simpler than it sounds, and it worked seamlessly, even temporarily turning off the music whenever a call comes on the car’s bluetooth.
    
    But it felt a bit weird to sitting there in my tiny car, with two active Bluetooth connections. Deep down, I couldn’t help worrying whether all those electromagnetic Bluetooth waves madly bouncing around inside the metal car were cooking up our brains.
    
    Yes, most of believe Bluetooth is harmless as everyone’s using it with seemingly no ill-effects. But then everyone used to happily smoke not so long ago, and nearly everyone is still swilling down tonnes of sugar without a care, in cokes, cakes and almost every other packaged food.
    
    What wouldn’t I give to travel twenty years into the future, and see science’s verdict on the effects of Bluetooth. But there’s only so much a Dad can do.
    
    As of now, the kids have their music, I have my phone, and all’s well in the world.
    

### Spell-Checking the tokenized words 


```python
d = enchant.Dict("en_US")
non_dict_words = list(set([word.encode('ascii', 'ignore') for word in word_tokenize(my_article.text) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] ))
non_dict_words
```




    ['USB', 'Bluetooth', 'bluetooth', 'blueteeth', 'eBay', 'handsfree']

## Oops - Not-so-intelligent Spell-Checker thinks these millenial words are non-English ;)
