from argparse import ArgumentParser
from functools import reduce

import operator
import sys

def main(argv):

    args = parse_args(argv)

    f = open(args.inputFilePath, 'r')
    
    result = 0
    for line in f:
        result += get_line_power(line)

    print("Result = {}".format(result))
    f.close()

    return

def get_line_power(line):

    draws = line.split(": ")[1].split("; ")
    maxdraws = get_max_draws(draws)
    gpower = reduce(operator.mul, maxdraws.values())
    return gpower

def get_max_draws(draws):
    
    maxdraws = {
        "red" : 0,
        "green" : 0, 
        "blue" : 0
    }

    for draw in draws:
        cubes = draw.split(", ")
        for cube in cubes:
            count = int(cube.split(" ")[0].strip())
            color = cube.split(" ")[1].strip()
            if count > maxdraws[color]:
                maxdraws[color] = count

    return maxdraws

def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument("-f", "--inputFilePath", help="Input data file filepath", dest="inputFilePath", required=True)
    args = parser.parse_args()
    return args


main(sys.argv[1:])