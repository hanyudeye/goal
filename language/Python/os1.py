import sys
print("os startup....")

str=""

while True:
    try:
        str=input("$>: ")
        print("run command",str)
    except KeyboardInterrupt:
        print("os exit")
        sys.exit(0)
