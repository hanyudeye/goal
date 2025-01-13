from urllib.request import urlopen
file=urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/').read()
print(file)