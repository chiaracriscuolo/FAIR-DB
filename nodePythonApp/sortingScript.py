## IMPORT LIBRARIES
import sys
import json
import pandas 
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

params = json.loads(sys.argv[1])
dataset = params['dataset']
file_path_acfds_json = '../static/ACFDs'+dataset+'Computed.json'
#with open('../static/ACFDsTitanicComputed.json') as f:
#    a_json = json.load(f)
#    df51 = pandas.DataFrame.from_dict(a_json, orient="columns")
orderingCriterion = params['orderingCriterion']
print("Ord criterion: ", type(orderingCriterion), orderingCriterion)
df51 = pandas.read_json(file_path_acfds_json, orient='split')

if(orderingCriterion == 'Support'):
    df6 = df51.iloc[df51['Support'].argsort()[::-1][:len(df51)]]
    print('Ordered by Support')
elif(orderingCriterion == 'Difference'):
    df6 = df51.iloc[df51['Diff'].argsort()[::-1][:len(df51)]]
    print('Ordered by Difference')
else:
    # df51['Mean'] = 0
    #for index, row in df51.iterrows():
    #     df51.loc[index, 'Mean'] = ((df51.loc[index, 'Support'] + df51.loc[index,'Diff'])/2)
    df6 = df51.iloc[df51['Mean'].argsort()[::-1][:len(df51)]]
    print('Ordered by Mean')

# Write JSON file
df6.to_json(path_or_buf='../static/ACFDs'+dataset+'Computed.json', orient="split")