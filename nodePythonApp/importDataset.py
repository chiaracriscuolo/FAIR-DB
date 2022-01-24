import sys
import json
import pandas 
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

path = sys.argv[1]
dataset = 'dataset'
df = pandas.read_csv(path)

if(dataset == 'Titanic' or dataset == 'dataset'):
    df = df.applymap(lambda x : str(x) if type(x) == int else x)
#EXTRA to extract a JSON FILE

# data = df.to_json(orient="split")
columnValues = {}
for c in list(df.columns):
    columnValues[c] = list(df[c].unique())
print(columnValues)
a_file = open('../static/'+dataset+'ColumnsValues.json', "w")
a_file = json.dump(columnValues, a_file)  

df.to_json(path_or_buf='../static/dataset.json', orient="split")
# df.name = 'preprocesseddataset.csv'
df.to_csv('../cdfAlgorithm/cfddiscovery/datasets/preprocesseddataset.csv', index=False)
# print(json.dumps(data))
# Write JSON file
#with io.open('../static/dataset.json', 'w', encoding='utf8') as outfile:
#    str_ = json.dumps(data,
#                      indent=4, sort_keys=True,
#                      separators=(',', ': '), ensure_ascii=False)
#    outfile.write(to_unicode(str_))

