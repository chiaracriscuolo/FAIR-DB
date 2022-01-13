import sys
import json
import pandas 
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

dataset = sys.argv[1]
path = sys.argv[2]

print("PATH: ", path)
