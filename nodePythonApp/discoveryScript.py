
## IMPORT LIBRARIES
import sys
import json
import pandas
import utils
#import numpy as np

########## SCRIPT TO DISCOVER ACFDS AND FILTER THEM ##########
######### 1. TAKE INPUTS #########

## The body of the request that contains all input parameters
y = json.loads(sys.argv[1])
#print(y)
#for property in y:
    #print(property + "=")
    #print(y[property])

protected_attr = y['protected_attr']
target = y['target']
confidence = y['confidence']
supportCount = y['supportCount']
maxAntSize = y['maxAntSize']
minDiff = y['difference']
dataset = y['dataset']

file_path = '../cdfAlgorithm/cfddiscovery/datasets/preprocessed'+dataset+'.csv'
df = pandas.read_csv(file_path)
all_tuples = len(df)
cols = df.columns
support = supportCount/all_tuples
## TODO Risolvere SupportCount!!
#supportCount = support*all_tuples
#print(cols, all_tuples, supportCount)
## To deal with numbers ##
if(dataset == 'Titanic' or dataset == 'dataset'):
    df = df.applymap(lambda x : str(x) if type(x) == int else x)

########## 2. APPLY CFD_DISCOVERY ALGORITHM ##########

#Apply CFDDiscovery algorithm
#output = !../cdfAlgorithm/cfddiscovery/CFDD {file_path} {supportCount} {confidence} {maxAntSize} | grep {grepValue}
outputDiscovery = sys.argv[2]
outputDiscovery = outputDiscovery.split('\n')

#to delete the final comment (strings) of cdfDiscovery
outputDiscovery.pop()
outputDiscovery.pop() 
# print(outputDiscovery)
#all rules obtained
#print("Total number of dependencies found: ", len(outputDiscovery), "\n")

#for i in range(0,2):
    #print("Dependency n.", i, ": " ,outputoutputDiscovery[i])

###### 3. TRASFORM CFD DISCOVERY OUTPUT IN A DICTIONARY ##########
#Transform the '<=' in '<' and viceversa to not have problem with the following '=' detection
o1 = list(map(lambda x: x.replace("<=", "<"), outputDiscovery))
#o1 = list(map(lambda x: x.replace(">=", ">"), output))
#Delete the parenthesis
o1 = list(map(lambda x: x.replace("(", ""), o1))
o1 = list(map(lambda x: x.replace(")", ""), o1))
#Split the entire rule in a lhs and rhs 
o2 = list(map(lambda x: x.split(' => '), o1))

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
    
    
#TODO ADD MANAGING OF CONDITIONS
#condition to delete some rules that are not interesting, for example:
#conditionslhs = ['age-range=15-30']
conditionslhs = []
conditionsrhs = []

o3 = list()   
if not conditionslhs and not conditionsrhs:
    for i in o2:
        x = parseCFD(i)
        if (x != None):
            o3.append(x)
else:
    for i in o2:
        x = parseCFDWithCond(i,conditionslhs, conditionsrhs)
        if (x != None):
            o3.append(x)
            
#for i in range(0,3):
#    print(o3[i])

#To split every couple attribute-value
def splitElem(l1):
    return list(map(lambda x: x.split('='), l1))

#To create an array that contains all rules with the lhs and rhs separated
def createSplitting(elem):
    elemLhs = elem[0]
    elemRhs = elem[1]
    LHS = splitElem(elemLhs)
    RHS = splitElem(elemRhs)
    return [LHS, RHS]

#Now that we have deleted all the '=' we can replace the "<" with '<='
def createDictionaryElem(side):
    elem = {}
    for x in side:
        replacedX = x[1].replace('<', '<=')
        elem[x[0]]= replacedX
    return elem

o4 = list(map(createSplitting, o3))
#for i in range(0,4):
#    print(o4[i])


#Create the dictionary with the LHS and RHS that contains all CFDs
parsedRules = list(map(lambda x: {'lhs' : createDictionaryElem(x[0]), 'rhs': createDictionaryElem(x[1])}, o4))

#print("Total number of STARTING dependencies in the dictionary: " ,len(parsedRules)

######### 4. COMPUTE THE TABLE OF ACFDS WITH METRICS #########
## FUNCTIONS NEEDED TO CREATE THE TABLE ##
import math

def countOccur(elem):
    #How many times appears the lhs of the rule
    countX = 0
    #How many times appears the rhs of the rule
    countY = 0
    #How many times appears the entire rule
    countXY = 0
    
    #for every row of the database, count the LHS, RHS and the total count
    for index, row in df.iterrows():
        #The flags help in dealing with missing values
        flagX = True
        flagY = True
        
        for key in list(elem['lhs'].keys()):
            value = elem['lhs'][key]
            
            #add the constraint to manage '?' that could be a missing values
            if (str(row[key]) != value):
                flagX = False
                
        for key in list(elem['rhs'].keys()):
            value = elem['rhs'][key]
            
            #add the constraint to manage missing values
            if (str(row[key]) != value):
                flagY = False
                
        if flagX:
            #increase the lhs support count
            countX = countX + 1
        if flagY:
             #increase the rhs support count
            countY = countY + 1
        if flagX and flagY:
             #increase the entire rule support count
            countXY = countXY + 1
    #return the lhs supp count, rhs supp count and the entire rule supp count 
    return  (countX, countY, countXY)

def computeConfidenceNoProtectedAttr(elem):
    
    filteredRule = {}
    filteredRule['lhs'] = {k: v for k, v in elem['lhs'].items() if ((k not in (protected_attr)) and (k != target))}
    filteredRule['rhs'] = elem['rhs']
    
    fCount = countOccur(filteredRule)
    #if the rule is valid for at least one tuple
    if(fCount[2] != 0 and fCount[0] != 0):
        ratio = fCount[2]/fCount[0]
    else: 
        ratio = 0
    return ratio

def computeConfidenceForProtectedAttr(elem, protAttr):
    
    filteredRule = {}
    filteredRule['lhs'] = {k: v for k, v in elem['lhs'].items() if (k != protAttr)}
    filteredRule['rhs'] = elem['rhs']
    
    fCount = countOccur(filteredRule)
    #if the rule is valid for at least one tuple
    if(fCount[2] != 0 and fCount[0] != 0):
        ratio = fCount[2]/fCount[0]
    else:
        ratio = 0
    return ratio

def computePDifference(rule, conf, attribute):
    if(attribute in protected_attr):
        diffp = 0
        if(attribute in rule['lhs'].keys()):
            RHSConfidence = computeConfidenceForProtectedAttr(rule, attribute)
            diffp = conf - RHSConfidence
            return diffp
    return None

def equalRules(rule1,rule2):

    flagR = True
    flagL = True
    
    for keyL in rule1['lhs'].keys():
        if(keyL in rule2['lhs'].keys()):
            if(rule1['lhs'][keyL]!=rule2['lhs'][keyL]):
                flagL = False
        else: 
            flagL = False
            
    for keyR in rule1['rhs'].keys():
        if(keyR in rule2['rhs'].keys()):
            if(rule1['rhs'][keyR]!=rule2['rhs'][keyR]):
                flagR = False
        else:
            flagR = False
            
    if(flagL==True and flagR == True):
        return True
    else:
        return False
    
def removeDuplicates(df):
    dfColumns = df.columns
    k=0
    dfClean= pandas.DataFrame(columns = dfColumns)
    for i, row in df.iterrows():
        flag = True
        rule1 = df.loc[i, 'Rule']
        j=k-1
        while(j>=0):
            rule2 = dfClean.loc[j, 'Rule']
            if(equalRules(rule1,rule2)==True):
                flag = False
            j=j-1
        if(flag == True):
            dfClean.loc[k] = df.loc[i]
            k=k+1
            
    return dfClean 
    
def removeDuplicatesArray(arrayList):
    
    cleanedArray = []
    k=0
    for i in range(0, len(arrayList)):
        flag = True
        rule1 = arrayList[i]
        j=k-1
        while(j>=0):
            rule2 = cleanedArray[j]
            if(equalRules(rule1,rule2)==True):
                flag = False
            j=j-1
        if(flag == True):
            cleanedArray.append(arrayList[i])
            k=k+1
            
    return cleanedArray

def createTable(parsedRules):
    df3 = pandas.DataFrame(columns=['Rule', 'Support', 'Confidence', 'Diff'])
    for attribute in protected_attr:
        column = attribute+'Diff'
        df3[column] = 0

    row_index = 0
    for i,parsedRule in enumerate(parsedRules):

        count = countOccur(parsedRule)
        support = tuple(map(lambda val: val/all_tuples, count))
        conf = 0
        confNoProtectedAttr = 0
        RHSConfidence = 0
        diff = 0
        flagProt = False
        flagTarget = False

        for keyL in parsedRule['lhs'].keys():
            if(keyL in protected_attr):
                flagProt = True
            if(keyL == target):
                flagTarget = True
        for keyR in parsedRule['rhs'].keys():
            if(keyR in protected_attr):
                flagProt = True
            if(keyR == target):
                flagTarget = True

        if(support[0]!= 0 and support[1]!=0 and flagProt == True and flagTarget == True):
            conf = count[2]/count[0]
            confNoProtectedAttr = computeConfidenceNoProtectedAttr(parsedRule)
            diff = conf - confNoProtectedAttr

            #lift = support[2]/(support[0]*support[1])


            df3 = df3.append({'Rule': parsedRule, 'Confidence': conf, 'Support': support[2], 'Diff': diff}, ignore_index=True)

             #compute the diff for each protected  attributes
            for attribute in protected_attr:
                diffp = 0
                if(attribute in parsedRule['lhs'].keys()):
                    diffp = computePDifference(parsedRule, conf, attribute)
                    column = attribute+'Diff'
                    df3.loc[row_index, column] = diffp 
            row_index = row_index +1
    return df3

#### END OF PART OF FUNCTIONS ####
df3 = createTable(parsedRules)
df3 = removeDuplicates(df3)
pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.max_rows', None)
df4 = df3[df3.Diff > minDiff]
#print("Total number of ACFDs (before completion) in dataframe after applying difference threshold: " ,len(df4))

####### 6. ACFDs COMPLETION ######
## FUNCTIONS NEED FOR THE CARTESIAN PRODUCT ##
def cartesianProduct(set_a, set_b): 
    result =[] 
    for i in range(0, len(set_a)): 
        for j in range(0, len(set_b)): 
  
            # for handling case having cartesian 
            # prodct first time of two sets 
            if (type(set_a[i]) != list):          
                set_a[i] = [set_a[i]] 
                  
            # coping all the members 
            # of set_a to temp 
            temp = [num for num in set_a[i]] 
              
            # add member of set_b to  
            # temp to have cartesian product      
            temp.append(set_b[j])              
            result.append(temp)   
              
    return result 


  
def Cartesian(list_a, n):
    # result of cartesian product 
    # of all the sets taken two at a time 
    temp = list_a[0] 
      
    # do product of N sets  
    for i in range(1, n): 
        temp = cartesianProduct(temp, list_a[i]) 
          
    return temp 

def createSide(side):
    elem = {}
    for x in side:
        elem[x[0]] = x[1]
    
    return elem

import copy
def findCFDsCombinations(elem):
    CFDs = []
    perm = []
    attr_names = []
    assocRule = list()
    flag = False
    #select db according to already set attributes
    for key in list(elem['lhs'].keys()):
        
        if((key in protected_attr) or (key == target)):
            attr_names.append(key)
            perm.append(df[key].unique())
            flag = True
            
            
    for key in list(elem['rhs'].keys()):
        
        if((key in protected_attr) or (key== target)):
            attr_names.append(key)
            perm.append(df[key].unique())
            flag = True
    
    if(flag == True):
        
        assocRule = copy.deepcopy(elem)
        mat =  Cartesian(perm, len(perm))

        for m in mat:
            if(len(attr_names) == 1):
                for key in list(assocRule['lhs'].keys()):
                    if(key == attr_names[0]):
                        assocRule['lhs'][key] = m
                for key in list(assocRule['rhs'].keys()):
                    if(key == attr_names[0]):
                        assocRule['rhs'][key] = m
            
            else:
                i= 0

                assocRule = copy.deepcopy(elem)
                while(i< len(m)):

                    for key in list(assocRule['lhs'].keys()):
                        if(key == attr_names[i]):
                            assocRule['lhs'][key] = m[i]
                    for key in list(assocRule['rhs'].keys()):
                        if(key == attr_names[i]):
                            assocRule['rhs'][key] = m[i]
                    i = i+1
                   
            CFDs.append(assocRule) 
        return CFDs 
    else:
        return elem

## END OF FUNCTION PART ##

CFDCombinations = []
for elem in df4.Rule:
    #for every rule compute the combinations over the protected attribute
    rulesCount = findCFDsCombinations(elem)
    
    for ar in rulesCount:
        CFDCombinations.append(ar)

CFDCombinations = removeDuplicatesArray(CFDCombinations)
#print("Total number of combinations found after removing duplicates: ", len(CFDCombinations))

####### 7. SHOW ACFDS COMPLETED #######
df5 = createTable(CFDCombinations)   
df5 = removeDuplicates(df5)
pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.max_rows', None)
df51 = df5[df5.Diff > minDiff]
#print("Total number of ACFDs (after completion) in dataframe after applying difference threshold: " ,len(df51))

########## 8. ORDER THE DEPENDENCIES ##########
#Order the rules by Diff or Support or Mean
## DEFAULT: ORDER BY MEAN ##
orderingCriterion = 2
if(orderingCriterion == 0):
    df6 = df51.iloc[df51['Support'].argsort()[::-1][:len(df51)]]
elif(orderingCriterion ==1):
    df6 = df51.iloc[df51['Diff'].argsort()[::-1][:len(df51)]]
else:
    df51['Mean'] = 0
    for index, row in df51.iterrows():
         df51.loc[index, 'Mean'] = ((df51.loc[index, 'Support'] + df51.loc[index,'Diff'])/2)
    df6 = df51.iloc[df51['Mean'].argsort()[::-1][:len(df51)]]
    
#print("Number of original ACFDs: ", len(df4), ". Number of ACFDs after completion: ", len(df5), ". Number of final ACFDs found: ", len(df6))
#df6.head()

##### 9. COMPUTE AND SAVE ACFDSTITANIC.JSON #####
import json
# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

df6 = df6.reset_index(drop=True)
to_save_path_csv = utils.get_absolute_path(__file__, '../static/ACFDs'+dataset+'Computed.csv')
#print("path*** "+ to_save_path_csv)
df6.to_csv(to_save_path_csv,index=True)
#df6.to_csv('../static/ACFDs'+dataset+'Computed.csv',index=True)

to_save_path_json = utils.get_absolute_path(__file__, '../static/ACFDs'+dataset+'Computed.json')
df6.to_json(path_or_buf=to_save_path_json, orient="split")
#df6.to_json(path_or_buf='../static/ACFDs'+dataset+'Computed.json', orient="split")

with io.open('../static/'+dataset+'Params.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(y,
                     indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))