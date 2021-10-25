## IMPORT LIBRARIES
import sys
import json
import pandas 
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

### Functions ###

def extractProblematicTuples(dfMarked):
    dfEthicalProblems = dfMarked[dfMarked.marked > nMarked]
    return dfEthicalProblems

def computeStatistics(df6, selectedDependencies, dfMarked, indexArray):

    scores = 0
    diffs = 0
    marks = dfMarked.marked.sum()
    
    for i in indexArray:
        scores = scores + df6.Mean[i]
        diffs = diffs + df6.Diff[i]

    scoreMean = (scores/len(selectedDependencies))
    diffMean = (diffs/len(selectedDependencies))
    pMean = 0

    dfM = dfMarked[dfMarked.marked != 0]
    #print(All tuples interested by the rules: ', marks)

    print('Number of tuples interested by the rules: ', len(dfM), ". Total number of tuples: ", len(df), "\n")
    print( "Cumulative Support: ", len(dfM)/len(df), ". Difference Mean: ", diffMean, "\n")

    for attribute in protected_attr:
        deps = 0
        if(attribute+'Diff' in df6):
            for i in indexArray:
                if not(pandas.isna(df6[attribute+'Diff'][i])):
                    #print(df6[attribute+'Diff'][i])
                    pMean = pMean + df6[attribute+'Diff'][i];
                    deps = deps+1
            if(pMean != 0):
                pMean = (pMean/deps)
                print(attribute, '-Difference Mean: ', pMean, "\n")

    finalRules =  df6[df6.index.isin(indexArray)]
    print("Total number of ACFDs selected: ", len(finalRules), "\n")
    return finalRules

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



file_path_acfds = '../static/ACFDsTitanicComputed.csv'
file_path = '../cdfAlgorithm/cfddiscovery/datasets/preprocessedTitanic.csv'
df = pandas.read_csv(file_path)
df6 = pandas.read_csv(file_path_acfds)
#add column 'marked'
#add one column to count the number of tuples involved by the dependencies
df['marked'] = 0

params = json.loads(sys.argv[1])
#orderingCriterion = params['orderingCriterion']
#indexArray = params['acfds']
indexArray = [1,2,3,4,5]
#minumum number of rules necessary to have a problematic tuple
nMarked = 0

dependencies = []
for i in indexArray:
    dependencies.append(df6.Rule[i])
    
#create a copy of the df to count the number of tuples involved by the dependencies
dfMarked = df
for dep in dependencies:
    #for every dependency add one to marked field if the tuple respect the rule
    validates(dfMarked, dep)

    
dfEthicalProblems = extractProblematicTuples(dfMarked)
print("Problematic tuples: ", len(dfEthicalProblems))

finalRules = computeStatistics(df6, dependencies, dfMarked, indexArray)

