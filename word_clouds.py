import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL.Image import Image
from wordcloud import WordCloud, STOPWORDS

# Download file from: https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/alice_novel.txt
# open the file and read it into a variable alice_novel
alice_novel = open('alice_novel.txt', 'r').read()
# print(alice_novel)

# Download image: https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Images/alice_mask.png
# How does Image.open works?
# alice_mask = np.array(Image.open('alice_mask.png'))

stopwords = set(STOPWORDS)  # set() removes reduntant stopwords (to, a, an, of...)

alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)

stopwords.add('said')

# generate the word cloud
alice_wc.generate(alice_novel)
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
