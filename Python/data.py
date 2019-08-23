'''
In this project, you will visualize the feelings and language used in
a set of Tweets. This starter code loads the appropriate libraries
and the Twitter data you'll need!
'''
from wordcloud import WordCloud
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

# Opens tweetFile
tweetFile = open("data.json" , "r")

#Get the JSON data
tweetData = json.load(tweetFile)

tweetFile.close()

# Continue your program below!
tb= TextBlob ("you are a brilliant computer scientist")
print(tb.polarity)

polarity =[]
subjectivity = []

for tweet in tweetData:
    
     testimonial = TextBlob(tweet["text"])
     testimonial.sentiment

     polarity.append(testimonial.sentiment.polarity)
     subjectivity.append(testimonial.sentiment.subjectivity)

print(polarity)
print(subjectivity)

plt.hist(polarity, 10, facecolor='purple', alpha=0.5)
plt.show()
plt.hist(subjectivity, 10, facecolor='yellow', alpha=0.5)
plt.show()
# testimonial.sentiment.polarity("you are a brilliant computer scientist.")

# Textblob sample:
