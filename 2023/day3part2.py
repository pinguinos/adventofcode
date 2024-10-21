import operator
import sys

from argparse import ArgumentParser
from collections import defaultdict
from functools import reduce

def main(argv):

    args = parse_arg(argv)
    f = open(args.inputFilePath, 'r')

    inputs = [line for line in f] # not stripping, using end of line "\n" as a buffer for symbol checking
    starMap = defaultdict(list)

    for rindx, row in enumerate(inputs):
        numstr = ""
        pstart = -1 
        for cindx, c in enumerate(row):
            if c.isdigit():
                numstr += c
                if pstart == -1:
                    pstart = cindx 
            else:
                if pstart != -1:
                    check_star_symbol(rindx ,pstart, numstr, inputs, starMap)

                pstart = -1
                numstr = ""

    result = compute_gear_ratio(starMap)
    print("Result = {}".format(result))
    return


def compute_gear_ratio(starMap):
    
    sumGratio = 0
    for v in starMap.values():
        if len(v) == 2:
            gratio = reduce(operator.mul, v)
            sumGratio += gratio

    return sumGratio
        

def check_star_symbol(rindx, pstart, numstr, inputs, starMap):

    for r in range(rindx-1, (rindx+1)+1): # +1 because range is not inclusive at end bound
        if r < 0 or r >= len(inputs):
            continue
        for c in range(pstart-1, ( pstart+len(numstr) ) + 1): 
            if c < 0 or c >= len(inputs[rindx]):
                continue
            if inputs[r][c] == "*":
                starMap[(r, c)].append(int(numstr))
    return
    


def parse_arg(argv):
    parser = ArgumentParser()
    parser.add_argument("-f", "--inputFilePath", help="Input data file filepath", dest="inputFilePath", required=True)
    args = parser.parse_args()
    return args

main(sys.argv[1:])