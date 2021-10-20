
import sys
import json
import pandas
#import numpy as np

#def return_key(currency_dict, val):
#    val_list = currency_dict.values()
#    key_list = currency_dict.keys()
#    found_key = []
#    for i in range(len(currency_dict)):
#        if val_list[i]==val:
#            found_key.append(key_list[i])
#    return("Key Not Found")

###### 1. TAKE INPUTS
#protected_attr = ['Pclass', 'Sex',]
#target = 'Survived'
#print('#Discovery script#')

y = json.loads(sys.argv[1])
#print(y)
#for property in y:
    #print(property + "=")
    #print(y[property])


protected_attr = y['protected_attr']
#list(dict_protected_attr.keys())[list(dict_protected_attr.values()).index(true)]
#for attr in protected_attrs:
#    if(y['protected_attr'].attr == 'true')
#    protected_attr.append(attr)

target = y['target']
confidence = y['confidence']
supportCount = y['supportCount']
maxAntSize = y['maxAntSize']
difference = y['difference']
#print(protected_attr, target, confidence, support, maxAntSize, difference)

#other parameters
grepValue = target+'='

file_path = '../cdfAlgorithm/cfddiscovery/datasets/preprocessedTitanic.csv'
df = pandas.read_csv(file_path)
all_tuples = len(df)
cols = df.columns
## TODO TOGLIERE COMMENTO!!
#supportCount = support*all_tuples
#print(cols, all_tuples, supportCount)

##### 2. APPLY CFD_DISCOVERY ALGORITHM

#Apply CFDDiscovery algorithm
#output = !../cdfAlgorithm/cfddiscovery/CFDD {file_path} {supportCount} {confidence} {maxAntSize} | grep {grepValue}
output = sys.argv[2]

#all rules obtained
#print("Total number of dependencies found: ", len(output), "\n")

#for i in range(0,2):
    #print("Dependency n.", i, ": " ,output[i])



#VARIE COMPUTAZIONI PER AVERE INDIETRO ACFDSTITANIC.JSON
