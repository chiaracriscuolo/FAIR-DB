## IMPORT LIBRARIES
import sys
import json
import pandas 
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

file_path = '../static/ACFDsTitanicComputed.csv'
#with open('../static/ACFDsTitanicComputed.json') as f:
#    a_json = json.load(f)
#    df51 = pandas.DataFrame.from_dict(a_json, orient="columns")
params = json.loads(sys.argv[1])
orderingCriterion = params['orderingCriterion']
print("Ord criterion: ", type(orderingCriterion), orderingCriterion)
df51 = pandas.read_csv(file_path)

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

df6.to_csv('../static/ACFDsTitanicComputed.csv',index=False)
data = df6.to_json(orient="split")
# Write JSON file
with io.open('../static/ACFDsTitanicComputed.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))