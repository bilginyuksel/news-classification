#import news #You can get news from there.
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
    #Step 1
    return content

def listModel(content):
    #Step 2
    return content.split(' ')

def conjuction_prepositions(word_list):
    #Step 3
    for i in __conjuctions_prepositions_TR:
        if i in word_list:
            word_list.remove(i)

    return word_list
