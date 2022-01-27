import sys
import json
import pandas 
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

########## SCRIPT TO IMPORT A CUSTOM DATASET ##########
path = sys.argv[1]
dataset = 'dataset'
df = pandas.read_csv(path)

#This is for managing integer in FAIR-DB
if(dataset == 'Titanic' or dataset == 'dataset'):
    df = df.applymap(lambda x : str(x) if type(x) == int else x)

# Extract json file from csv and save it
columnValues = {}
for c in list(df.columns):
    columnValues[c] = list(df[c].unique())
print(columnValues)
a_file = open('../static/'+dataset+'ColumnsValues.json', "w")
a_file = json.dump(columnValues, a_file)  

df.to_json(path_or_buf='../static/dataset.json', orient="split")

df.to_csv('../cdfAlgorithm/cfddiscovery/datasets/preprocesseddataset.csv', index=False)


