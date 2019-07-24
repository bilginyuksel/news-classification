import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm


data = pd.read_csv('data.csv')

# find useless attributes on dataset
useless_attributes = [col for col in data.columns if data[col].std()==0]
# when you find the useless attributes drop all columns
data.drop(useless_attributes,axis=1,inplace=True)

# create categories


data['Category'] = "none"

# <Ekonomi> News : 220
# <Spor> News : 220
# <Politika> News : 240
# <Yasam> News : 220
# <Dunya> News : 200

data.loc[0:220,'Category'] = "ekonomi"
data.loc[220:440,'Category'] = "spor"
data.loc[440:680,'Category'] = "politika"
data.loc[680:900,'Category'] = "yasam"
data.loc[900:1100,'Category'] = "dunya"

# continue with clean data
clear_data = data.loc[:899]

# cross validation
train_x,test_x,train_y,test_y = train_test_split(clear_data.drop('Category',axis=1),clear_data.Category,test_size =0.2)

models = {'K-nn':KNeighborsClassifier(n_neighbors = 15),
'RandomForest':RandomForestClassifier(),
'DecisionTree':DecisionTreeClassifier(),
'SVM':svm.SVC(gamma = 1,C=0.8)}
# create knn object
# knn = KNeighborsClassifier(n_neighbors = 15)
# knn.fit(train_x,train_y)

print()
#fit data
for i in models.values():
    i.fit(train_x,train_y)

#find models scores
for i,j in zip(models.keys(),models.values()):
    print(i,"guesses :",j.score(test_x,test_y))


# predict test data


# model_predicts = knn.predict(test_x)
# model_predicts = models['knn'].predict(test_x)
# test_y = np.array(test_y)

# true_guess = 0
# for i in range(len(model_predicts)):
#     if model_predicts[i] == test_y[i]:
#         true_guess+=1

# print("True guesses :",true_guess)
# print('Model accuracy :',models['RandomForest'].score(test_x,test_y))

