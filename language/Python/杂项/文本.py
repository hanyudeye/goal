line = 'asdf fjdk; afed, fjek,asdf, foo，你好.yes'


import re

# print(re.split(r'[;,\s，。.]\s*',line))
# print(re.split(r'[;,\s，。.]',line))

fields=re.split(r'(;|,|\s)\s*',line)
print(fields)
