

import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


""" Function to import data """
def ImportData(source_data, column_name):
    df = pd.read_csv(source_data)
    res = df[column_name][0]
    res = " ".join(map(str, df[column_name]))

    return res


""" Function to set stopwords """
def SetStopwords(stopwords):
    res = set(STOPWORDS)
    res.update(stopwords)

    return res


""" Function to generate wordcloud

    source_data
    column_name
    stopwords
    mask            image url to be used as mask
    colormap        Available values: https://matplotlib.org/tutorials/colors/colormaps.html
    font
    uppercase       True, False
    plot            True, False
    export          True, False

    """
def CreateWordcloud(source_data, column_name, stopwords, 
                    mask='input/mask.png', colormap='BrBG', font='input/font.TTF',
                    uppercase=True, plot=True, export=True):

    # Import data
    text = ImportData(source_data, column_name)

    # Set stopwords
    stopwords = SetStopwords(stopwords)

    # Set case
    if (uppercase == True):
        text = text.upper()
    else:
        text = text.lower()

    # Create mask
    mask = np.array(Image.open(mask))

    # Set wordcloud attributes
    wordcloud = WordCloud(stopwords=stopwords, 
                        font_path=font,
                        max_font_size=200, 
                        max_words=100, 
                        background_color='rgba(255, 255, 255, 0)',      # transparent background
                        mode='RGBA',
                        colormap=colormap,
                        mask=mask).generate(text)

    # Plot wordcloud
    if (plot == True):
        plt.figure()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.margins(x=0, y=0)
        plt.show()

    # Export wordcloud
    if (export == True):
        wordcloud.to_file('output/wordcloud.png')


# Set the path to csv file that contains the data
source_data='input/file.csv'

# Specify the column that contains the words to be used for the wordcloud
column_name='column_name'

# Specify any words to exclude from the wordcloud
stopwords=[]

# Generate wordcloud
CreateWordcloud(source_data, column_name, stopwords, 
                colormap='inferno',                 # Set colour schema
                font='input/font.TTF',              # Set font
                uppercase=False, 
                plot=False)