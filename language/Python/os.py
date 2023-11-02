import os

on_rtd=os.environ.get('PATH',None) 
# print(on_rtd)

filename=os.environ.get('PYTHONSTARTUP')
print(filename)
