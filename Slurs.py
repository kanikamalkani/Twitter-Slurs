# -*- coding: utf-8 -*-
"""


@author: kanik
"""

#importing the necessary libraries
import pandas as pd
import re

#Assumptions - All the racials slurs are included in the set created(racial_slurs)


# Step 1: Read the file and extract each tweet as a separate sentence.
with open('tweets.txt', 'r') as f:
    tweets = f.read().splitlines()

# Step 2: Load the set of words that indicate racial slurs.
racial_slurs = {'slur1', 'slur2', 'slur3', ...}

# Step 3: For each sentence, count the number of racial slurs present.
def count_slurs(sentence):
    count = 0
    for word in sentence.split():
        if word.lower() in racial_slurs:
            count += 1
    return count

# Step 4: Calculate the degree of profanity based on the count of racial slurs.
for tweet in tweets:
    num_slurs = count_slurs(tweet)
    if num_slurs == 0:
        print(tweet, "- Clean")
    elif num_slurs == 1:
        print(tweet, "- Mild")
    elif num_slurs <= 3:
        print(tweet, "- Moderate")
    else:
        print(tweet, "- Severe")
