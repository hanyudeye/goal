

import argparse
from pathlib import Path

def parse_arguments():
    parse=argparse.ArgumentParser()
    parse.add_argument('pattern',type=str,nargs=1)
    parse.add_argument('start',type=str,nargs=1)
    parse.add_argument('-r',action='store_true')

    return parse.parse_args()



args=parse_arguments()

if args.r:
    start_path=Path(args.start[0])
    print(start_path)

else:
    print("gggd")