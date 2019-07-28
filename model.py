from train import randomforest_predict,model_columns
import prepare_news as pn
import pandas
import sys

# sys.argv[1] file name

f = open(sys.argv[1])
_news_from_file = f.read()
news = pn.conjuction_prepositions(pn.listModel(pn.clear(_news_from_file)))

#prepare news
col = model_columns()
data = {}
for i in col:
    data[i] = [0]

for j in news:
    for k in col:
        if k in j:
            data[k][0]+=1
summ = 0
for i in col:
    summ += data[i][0]

for i in col:
    if summ!=0:
        data[i][0] /= summ
#prepare news
data = pandas.DataFrame(data)


category = randomforest_predict(data)

print("""
*************************************** Our Models Prediction ************************************************\n""")
print(category)


print("""
*************************************** Actual Category ************************************************\n""")
print("Ekonomi")