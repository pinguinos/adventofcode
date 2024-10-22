import sys
import operator
import re

from argparse import ArgumentParser
from functools import reduce

def main(argv):

    args = parse_args()

    f = open(args.inputFilePath, 'r')
    lines = [line.strip() for line in f]

    countMap = {key: 1 for key in range(1, len(lines)+1)}

    for indx, line in enumerate(lines):
        cardNo = indx + 1
        nextcardNo = cardNo + 1
        matches = get_match_from_card(line)
        for card in range(nextcardNo, nextcardNo+len(matches)):
            countMap[card] = countMap[card] + countMap[cardNo]  


    result = reduce(operator.add, countMap.values())
    print("Result = {}".format(result))
    return


def get_match_from_card(line):
    tokens = line.split(": ")
    ptokens = tokens[1].split(" | ")
    
    winNums = re.split(r'\s+' ,ptokens[0].strip())
    myNums = re.split(r'\s+', ptokens[1].strip())
    return list( set(winNums) & set(myNums) ) 



def parse_args():

    parser = ArgumentParser()
    parser.add_argument("-f", "--inputFilePath", dest="inputFilePath", required=True)
    args = parser.parse_args()
    return args

main(sys.argv[1:])