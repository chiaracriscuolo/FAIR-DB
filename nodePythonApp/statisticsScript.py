## IMPORT LIBRARIES
import sys
import json
import pandas 
import io
import utils
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

########## SCRIPT TO COMPUTE THE STATISTICS GIVEN THE USER-SELECTED DEPENDENCIES ##########

### Functions ###

def extractProblematicTuples(dfMarked):
    dfEthicalProblems = dfMarked[dfMarked.marked > nMarked]
    return dfEthicalProblems

def computeStatistics(df6, selectedDependencies, dfMarked, indexArray):

    scores = 0
    diffs = 0
    marks = dfMarked.marked.sum()
    metrics = {}

    for i in indexArray:
        scores = scores + df6.Mean[i]
        diffs = diffs + df6.Diff[i]

    scoreMean = (scores/len(selectedDependencies))
    diffMean = (diffs/len(selectedDependencies))
    pMean = 0

    dfM = dfMarked[dfMarked.marked != 0]
    #print(All tuples interested by the rules: ', marks)

    #print('Number of tuples interested by the rules: ', len(dfM), ". Total number of tuples: ", len(df), "\n")
    #print( "Cumulative Support: ", len(dfM)/len(df), ". Difference Mean: ", diffMean, "\n")

    metrics['cumulativeSupport'] = len(dfM)/len(df)
    metrics['differenceMean'] = diffMean
    metrics['totTuples'] =  len(df)
    metrics['totTuplesInterested'] = len(dfM)
    pDiffs = {}

    for attribute in columns:
        deps = 0
        pMean = 0
        if(attribute+'Diff' in df6):
            for i in indexArray:
                if not(pandas.isna(df6[attribute+'Diff'][i])):
                    #print(df6[attribute+'Diff'][i])
                    pMean = pMean + df6[attribute+'Diff'][i];
                    deps = deps+1
            if(pMean != 0):
                pMean = (pMean/deps)
                #print(attribute, '-Difference Mean: ', pMean, "\n")
                pDiffs[attribute] = pMean

    metrics['pDiffs'] = pDiffs
    finalRules =  df6[df6.index.isin(indexArray)]
    #print("Total number of ACFDs selected: ", len(finalRules), "\n")
    return finalRules, metrics

#for every rule = elem, iter over all rows and add one if the tuple respect the rule
def validates(df,elem):  
    
    for index, row in df.iterrows():
        flag = True
        for key in list(elem['lhs'].keys()):
            value = elem['lhs'][key]

            #add the constraint to manage '?' that could be a missing values
            if (str(row[key]) != value):
                flag = False
            

        for key in list(elem['rhs'].keys()):
            value = elem['rhs'][key]

            #add the constraint to manage missing values
            if (str(row[key]) != value):
                flag = False
                
        if(flag == True):
            #update the marked field
            df.loc[index, 'marked'] = df.loc[index, 'marked'] + 1

### End of function part ###

params = json.loads(sys.argv[1])
dataset = params['dataset']

file_path_acfds_json = utils.get_absolute_path(__file__, '../static/ACFDs'+dataset+'Computed.json')
#file_path_acfds_json = '../static/ACFDs'+dataset+'Computed.json'
file_path = utils.get_absolute_path(__file__, '../cdfAlgorithm/cfddiscovery/datasets/preprocessed'+dataset+'.csv')
#file_path = '../cdfAlgorithm/cfddiscovery/datasets/preprocessed'+dataset+'.csv'
df = pandas.read_csv(file_path)

df6 = pandas.read_json(file_path_acfds_json, orient='split')
columns = df.columns
#add column 'marked'
#add one column to count the number of tuples involved by the dependencies
df['marked'] = 0

#orderingCriterion = params['orderingCriterion']
indexArray = params['acfds']
#indexArray = [1,2,3,4,5]
#minumum number of rules necessary to have a problematic tuple
nMarked = 0
metrics = {}

dependencies = []
for i in indexArray:
    #print(df6.Rule[i])
    dependencies.append(df6.Rule[i])

#print(dependencies)   
#create a copy of the df to count the number of tuples involved by the dependencies
dfMarked = df
for dep in dependencies:
    #for every dependency add one to marked field if the tuple respect the rule
    validates(dfMarked, dep)

    
dfEthicalProblems = extractProblematicTuples(dfMarked)
#print("Problematic tuples: ", len(dfEthicalProblems))

to_save_path_json = utils.get_absolute_path(__file__,'../static/'+dataset+'ProblematicTuples.json')
dfEthicalProblems.to_json(path_or_buf=to_save_path_json, orient="split")

statistics = computeStatistics(df6, dependencies, dfMarked, indexArray)

finalRules = statistics[0]

to_save_path2_json = utils.get_absolute_path(__file__,'../static/'+dataset+'FinalACFDs.json')
finalRules.to_json(path_or_buf=to_save_path2_json, orient="split")

metrics = statistics[1]

## COMPUTE FAVOURED /DISCRIMINATED GROUPS 
def getTargetValue(ACFD):
    for key in list(ACFD['lhs'].keys()):
        
        if(key == target):
            return ACFD['lhs'][key]    
            
    for key in list(ACFD['rhs'].keys()):
        
        if(key== target):
            return ACFD['rhs'][key]
    return None

def selectRulesOnTargetValue(ACFDList):
    positiveTargetRules = []
    negativeTargetRules = []
    for ACFD in ACFDList:
        value = getTargetValue(ACFD)
        if(value != None):
            if(value == str(binaryValues[1])):
                positiveTargetRules.append(ACFD)
            else:
                negativeTargetRules.append(ACFD)
    return positiveTargetRules, negativeTargetRules

def getAttributeValue(ACFD, attribute):
    for key in list(ACFD['lhs'].keys()):
        
        if(key == attribute):
            return ACFD['lhs'][key]    
            
    for key in list(ACFD['rhs'].keys()):
        
        if(key== attribute):
            return ACFD['rhs'][key]
    return None

def selectAttributeValues(ACFDList, protected_attr):
    values = {}
    for attribute in protected_attr:
        v = []
        for ACFD in ACFDList:
            for a in ACFD['lhs'].keys():
                if (attribute == a):
                    value = getAttributeValue(ACFD, attribute)
                    if not(value in v):
                        v.append(value)
            for a in ACFD['rhs'].keys():
                if (attribute  == a):
                    value = getAttributeValue(ACFD, attribute)
                    if not(value in v):
                        v.append(value)
        values[attribute] = v
    return values

with open('../static/'+dataset+'Params.json') as f:
  params = json.load(f)

target = params['target']
protected_attr = params['protected_attr']
binaryValues = df[target].unique()
if (dataset == 'dataset'): 
    negativeTargetValue = params['negativeTargetValue']
    if (binaryValues[0] != negativeTargetValue):
        binaryValues[1] = binaryValues[0]
        binaryValues[0] = negativeTargetValue

rules = selectRulesOnTargetValue(dependencies)
positiveRules = rules[0]
negativeRules = rules[1]

#print("Positive rules: ", positiveRules)
#print("Negative rules: ", negativeRules)

favoured_groups= selectAttributeValues(positiveRules, protected_attr)
discriminated_groups= selectAttributeValues(negativeRules, protected_attr)

#print("Favoured rules: ", favoured_groups)
#print("Discriminated rules: ", discriminated_groups)

metrics['favoured'] = favoured_groups
metrics['discriminated'] = discriminated_groups

#print("FINAL METRICS:", metrics)
with io.open('../static/'+dataset+'Metrics.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(metrics,
                     indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

