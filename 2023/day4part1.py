import sys
import re

from argparse import ArgumentParser


def main(argv):

    args = parse_args(argv)
    f = open(args.inputFilePath, 'r')

    tpoints = 0
    for line in f:
        matches = get_match_from_card(line)
        point = get_point(matches)
        tpoints += point

    print("Result = {}".format(tpoints))
    return


def get_match_from_card(line):
    tokens = line.split(": ")
    ptokens = tokens[1].split(" | ")
    
    winNums = re.split(r'\s+' ,ptokens[0].strip())
    myNums = re.split(r'\s+', ptokens[1].strip())

    return list( set(winNums) & set(myNums) )

def get_point(matches):

    numMatches = len(matches)
    point = 0 if numMatches == 0 else pow(2, numMatches-1)
    return point

def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument("-f", "--inputFilePath", dest="inputFilePath", required=True)
    args = parser.parse_args()
    return args

main(sys.argv[1:])