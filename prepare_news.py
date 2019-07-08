#import news #You can get news from there.
import string
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from collections import Counter
import pandas as pd
#or any excell file doesn't matter.

"""
we have news that we can read but our machine learning model can't. Because of this we
have to prepare news for our machine learning model. So how can we do
this, first our news should a list that contains only words. Let me give
you an example:
    news_content = ["This summer python programming language is going to rise."]
    first of all we dont want any dots(.) .
    news_content = ["This summer python programming language is going to rise"]
    then let's do what we wanted first
    news_content = ['This','summer','python','programming','language','is','going','to','rise']
    conjuctions and prepositions worthless for our model.
    so lets clear our model one more step
    news_content = ['summer','python','programming','language','rise']
    Data Model:
    Id summer python programming language rise
    0  20%    20%    20%          20%     20%
    or better way
    Id summer python programming language rise
    0  0.5    0.5    0.5          0.5     0.5
    When we get a data model like this. We can train our machine learning model
"""
__conjuctions_prepositions_TR = [] #constant conjuctions and prepositions for removal
__model_columns = [] #Means words that model contains
#our training data has to give us the information about model columns.


def clear(content):
    new_content1 = content.replace('©','')
    new_content2 = new_content1.translate(str.maketrans('','',string.punctuation))
    return new_content2

def listModel(new_content2):
    new_content3 =  new_content2.split(' ')
    while '' in new_content3:
        new_content3.remove('')
    while '\n' in new_content3:
        new_content3.remove('\n')
    new_content3 = [x.lower() for x in new_content3]

    return new_content3

__conjuctions_prepositions_TR = stopwords.words('turkish')

def conjuction_prepositions(word_list):
    #Step 3
    for i in __conjuctions_prepositions_TR:
        for word in word_list:
            if word == i:
                word_list.remove(i)

    return word_list

def create_model(list_words):

    unique_word_list =  list(Counter(list_words).keys())
    counter_of_list = list(Counter(list_words).values())
    df = pd.DataFrame(counter_of_list)
    df = df.transpose()
    df.columns = unique_word_list
    df =  df.sort_values(by = 0, axis=1, ascending=False)
    return df

def frequency(dataframe):
    updated_dataframe = dataframe.apply(lambda x: x / int(dataframe.sum(axis=1)), axis=1)
    return  updated_dataframe

def final_cleaning(final_data):
    word_list = ['bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz','sıfır']
    for i in word_list:
        for item in final_data:
            if item == i:
                final_data.remove(i)
    for item in final_data:
        item = item.replace("'",'')
        item = item.replace('nin','')
        item = item.replace('ni','')

    return final_data


