
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
support = supportCount/all_tuples
## TODO Risolvere SupportCount!!
#supportCount = support*all_tuples
#print(cols, all_tuples, supportCount)

##### 2. APPLY CFD_DISCOVERY ALGORITHM

#Apply CFDDiscovery algorithm
#output = !../cdfAlgorithm/cfddiscovery/CFDD {file_path} {supportCount} {confidence} {maxAntSize} | grep {grepValue}
output = sys.argv[2]
print("Out: ", output)
print(type(output))
o_middle = output.split('\n')
print(type(o_middle), o_middle[0])

#all rules obtained
#print("Total number of dependencies found: ", len(output), "\n")

#for i in range(0,2):
    #print("Dependency n.", i, ": " ,output[i])

##TRASFORMARE OUTPUT DEL CFD DISCOVERY IN UN DIZIONARIO
#Transform the '<=' in '<' and viceversa to not have problem with the following '=' detection
o1 = list(map(lambda x: x.replace("<=", "<"), o_middle))
#o1 = list(map(lambda x: x.replace(">=", ">"), output))
#Delete the parenthesis
o1 = list(map(lambda x: x.replace("(", ""), o1))
o1 = list(map(lambda x: x.replace(")", ""), o1))
#Split the entire rule in a lhs and rhs 
#print(o1)
o2 = list(map(lambda x: x.split(' => '), o1))

print(o2)

#Function to select only CFDs from all rules
#x is the single rule
def parseCFD(x):
    #Flag indicates if the rule is a CFD (True) or and FD (False)
    isCFD = True
    rawLHS = x[0].split(', ')
    #lhs rule
    for i, y in enumerate(rawLHS):
        for attr in cols:
            if (y in str(attr+'=!')):
                isCFD = False
        
       
    rawRHS = x[1].split(', ')
    for i, y in enumerate(rawRHS):
        for attr in cols:
            if (y in str(attr+'=!')):
                isCFD = False
      
        #To keep only CFDs
        if(isCFD == True):
            return [rawLHS, rawRHS]
        else:
            return None
        
#conditions is an array of conditions to delete some rules that are not interesting, for example:
#  ex: conditionslhs = ['age-range=15-30', 'native-country=NC-White']     

def parseCFDWithCond(x, conditionslhs, conditionsrhs):
    #Flag indicates if the rule is a CFD (True) or and FD (False)
    isCFD = True
    #Flag indicates if the rule contains unwanted condition(s) (rhs or lhs) - it doesn't contain the condition (true)
    takenRule = True
    rawLHS= x[0].split(', ')
    #lhs rule
    for i, y in enumerate(rawLHS):
        for attr in cols:
            if (y in str(attr+'=!')):
                isCFD = False
            for condlhs in conditionslhs:
                if (y == condlhs):
                    takenRule = False
        
       
    rawRHS = x[1].split(', ')
    for i, y in enumerate(rawRHS):
        for attr in cols:
            if (y in str(attr+'=!')):
                isCFD = False
            for condrhs in conditionsrhs:
                if (y == condrhs):
                    takenRule = False
      
        #To keep only CFDs
        if(isCFD == True and takenRule == True):
            return [rawLHS, rawRHS]
        else:
            return None
    
    
#condition to delete some rules that are not interesting, for example:
#conditionslhs = ['age-range=15-30']
conditionslhs = []
conditionsrhs = []



#VARIE COMPUTAZIONI PER AVERE INDIETRO ACFDSTITANIC.JSON
