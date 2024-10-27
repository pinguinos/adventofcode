import sys
from argparse import ArgumentParser 

# Run command: python3 day5part1.py -inputFilePath inputs/day5.dat

def main(argv):

    seedsRaw = "4188359137 37519573 3736161691 172346126 2590035450 66446591 209124047 106578880 1404892542 30069991 3014689843 117426545 2169439765 226325492 1511958436 177344330 1822605035 51025110 382778843 823998526"
    seedsStr = seedsRaw.strip().split(" ")
    seeds = [int(seed) for seed in seedsStr]

    args = parse_args(argv)
    f = open(args.inputFilePath, 'r')

    seedRoutingLists = load_seed_routing_list(f)

    seedToLoc = dict()
    for seed in seeds:
        location = find_location(seed, seedRoutingLists)
        seedToLoc[seed] = location
    
    locs = seedToLoc.values()
    result = min(locs)
    print("Result is = {}".format(result))
    return
    

def find_location(seed, seedRoutingLists):

    for seedRoutingList in seedRoutingLists:
        for routeTuple in seedRoutingList:
            if seed >= routeTuple[0] and seed <= routeTuple[0] + routeTuple[2]:
                dest = routeTuple[1] + (seed - routeTuple[0])
                seed = dest
                break
        
    return seed 


def load_seed_routing_list(f):

    seedRoutingList = list()
    rowIndx =-1 

    for line in f:

        line = line.strip()
        if not len(line):
            continue

        if ":" in line:
            seedRoutingList.append(list())
            rowIndx += 1
            continue

        tokens = line.split(" ")
        routeTuple = ( int(tokens[1]), int(tokens[0]), int(tokens[2]) )
        seedRoutingList[rowIndx].append(routeTuple)

    return seedRoutingList


def parse_args(argv):

    parser = ArgumentParser()
    parser.add_argument("-f", "-inputFilePath", dest="inputFilePath", required=True)
    args = parser.parse_args(argv)
    return args

main(sys.argv[1:])