import operator
import sys

from argparse import ArgumentParser
from functools import reduce

def main(argv):

    args = parse_arg(argv)
    f = open(args.inputFilePath, 'r')

    inputs = [line for line in f] # not stripping, using end of line "\n" as a buffer for symbol checking
    nums = []

    for rindx, row in enumerate(inputs):
        numstr = ""
        pstart = -1 
        numprint = "" 
        for cindx, c in enumerate(row):
            if c.isdigit():
                numstr += c
                if pstart == -1:
                    pstart = cindx 
            else:
                if pstart != -1:
                    if has_surround_symbol(rindx ,pstart, numstr, inputs):
                        nums.append( int(numstr.strip()) )
                        numprint += (numstr + ", ")

                pstart = -1
                numstr = ""

    result = reduce(operator.add, nums)
    print("Result = {}".format(result))
    return


def has_surround_symbol(rindx, pstart, numstr, inputs):

    for r in range(rindx-1, (rindx+1)+1): # +1 because range is not inclusive at end bound
        if r < 0 or r >= len(inputs):
            continue
        for c in range(pstart-1, ( pstart+len(numstr) ) + 1): 
            if c < 0 or c >= len(inputs[rindx]):
                continue
            if not inputs[r][c].isdigit() and inputs[r][c] != "." and inputs[r][c] != "\n":
                return True
    return False
    



def parse_arg(argv):
    parser = ArgumentParser()
    parser.add_argument("-f", "--inputFilePath", help="Input data file filepath", dest="inputFilePath", required=True)
    args = parser.parse_args()
    return args

main(sys.argv[1:])