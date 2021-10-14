
import sys
import json

protected_attr = ['Pclass', 'Sex',]
target = 'Survived'
#print('#Discovery script#')

y = json.loads(sys.argv[1])
print(y)
#for property in y:
    #print(property + "=")
    #print(y[property])

#for attr in protected_attrs:
    #print(attr)

#print(target)

#VARIE COMPUTAZIONI PER AVERE INDIETRO ACFDSTITANIC.JSON