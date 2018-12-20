# Import libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as pyplot

# Read the text
with open("alice_in_wonderland.txt") as f:
    text = f.read()

# Set up the wordcloud variable
wordcloud = WordCloud(width=1920, height=1200)

# Add words that should be ignored
STOPWORDS.add('said')
STOPWORDS.add('illustation')

# Generate the wordcloud text
wordcloud.generate(text)

# Use matplotlib to visualize the words
pyplot.imshow(wordcloud, interpolation='bilinear')
pyplot.axis('off')
pyplot.show()