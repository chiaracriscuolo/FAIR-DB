# Test Script
import sys
import json
print('#Hello from python#')
#for property in sys.argv[1]:
    #print(property)
    #print(property + "=" + sys.argv[1][property])
    #print('First param:'+sys.argv[1]+'#')
#print('First param:'+sys.argv[1]+'#')
#json.dumps(sys.argv[1], separators=(',', ':'))
y = json.loads(sys.argv[1])
for property in y:
    print(property + "=")
    print(y[property])
#print(y)
print('Second param:'+sys.argv[2]+'#')