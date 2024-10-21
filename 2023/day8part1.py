# Traverse the graph following a fixed set of direction (left, right)
# Each node in the graph is connected to two adjust nodes: left node, right node
# Start node is always "AAA", ending node is always "ZZZ" after traversing the
# map following input directions: L (left), R (right)

def main():

    directions = "LRRLRRLRLLLRLLRLRRLRRLRRLRRLLRLLRRRLRRRLRRLLLRLRRLLLLLRRRLRRRLRRRLRRLRRLRLRLRLRLRRRLRRRLRRRLRRLRRLRLRLRRLLRRRLLRRLRRLRRRLRLLRRLRRLRRRLRRRLRRRLRRRLRRLLLRRRLLRRLLLRRLRRLLRRLRRRLRRLRRLRRRLRRLLLRLRRRLLRRRLRLRRLRLRLRLRRRLRLRLRRLLRRLRRLRRLRRLLRLRLRRRLRRLRRLRRLRLRRRLRRLRLLRRLLRRLRLLLRLLRRRLRLRLLRRRR"

    # load input graph into hashmap
    hashmapInputGraph = {}
    f = open('input/day8.dat', 'r')
    for line in f:
        tokens = line.split(" = ")
        pnode = tokens[0]
        childNodes = [tokens[1][1:4], tokens[1][6:9]]
        hashmapInputGraph[pnode] = childNodes
    f.close()

    # start walk the map
    steps = traverse(directions, hashmapInputGraph)
    print("Steps = {}".format(steps))

def traverse(directions, hashmapInputGraph):

    node = "AAA"
    step = 0

    while True: 

        for direction in directions:

            if node == "ZZZ":
                return step 

            indx = 0 if direction == "L" else 1
            node = hashmapInputGraph[node][indx]
            step = step + 1


if __name__ == "__main__":
    main()