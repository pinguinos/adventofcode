# Traverse the graph following a fixed set of direction (left, right)
# Each node in the graph is connected to two adjust nodes: left node, right node

def main():

    directions = "LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"

    # load input graph into hashmap
    hashmapInputGraph = {}
    f = open('input/day8part1.dat', 'r')
    for line in f:
        tokens = line.split(" = ")
        pnode = tokens[0]
        childNodes = [tokens[1][1:4], tokens[1][6:9]]
        hashmapInputGraph[pnode] = childNodes
    f.close()

    # local all starting nodes
    snodes = findStartingNodes(hashmapInputGraph)

    # start walk the map
    steps = traverse(snodes, directions, hashmapInputGraph)
    print("Steps = {}".format(steps))

def findStartingNodes(hashmapInputGraph):
    snodes = []
    for node in hashmapInputGraph:
        if node[-1] == "A":
            snodes.append(node)
    return snodes

def allNodesEndInZ(nodes):

    allNodesEndZ = True 
    for node in nodes:
        if node[-1] != "Z":
            allNodesEndZ = False
    return allNodesEndZ

def nextSetOfNodes(snodes, hashmapInputGraph, direction):
    nnodes= []

    indx = 0 if direction == "L" else 1
    for snode in snodes:
        nnode = hashmapInputGraph[snode][indx] 
        nnodes.append(nnode)

    return nnodes

def traverse(snodes, directions, hashmapInputGraph):

    step = 0
    while True: 

        for direction in directions:

            if allNodesEndInZ(snodes):
                return step

            snodes = nextSetOfNodes(snodes, hashmapInputGraph, direction)
            step = step + 1


if __name__ == "__main__":
    main()