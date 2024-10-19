import sys
from argparse import ArgumentParser

BAG = {
    "red": 12,
    "green" : 13,
    "blue" : 14
}

def main(argv):

    args = parse_arg(argv)

    print("Opening input data file {}".format(args.inputFilePath))
    f = open(args.inputFilePath, 'r')

    gsum = 0
    for line in f:
        gsum += validateAndRetrieveGameNumber(line)

    print("Game sum = {}".format(gsum))
    f.close()
    return

def validateAndRetrieveGameNumber(line):

    tokens = line.split(": ")
    gnumTokens = tokens[0].split(" ")
    gnum = int(gnumTokens[1])

    draws = tokens[1].split("; ")
    for draw in draws:
        cubes = draw.split(", ")

        for cube in cubes:
            cubeTokens = cube.split(" ")
            count = int(cubeTokens[0])
            color = cubeTokens[1]
            if count > BAG[color.strip()]:
                return gnum := 0

    return gnum

def parse_arg(argv):

    parser = ArgumentParser()
    parser.add_argument("-f", "--inputFilePath", help="Input data file filepath", dest="inputFilePath", required=True)
    args = parser.parse_args()
    return args

main(sys.argv[1:])