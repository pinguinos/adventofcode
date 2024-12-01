from collections import defaultdict

def main():

    f = open('inputs/day1.dat', 'r')

    left = list()
    right = defaultdict(int)

    for line in f:
        tokens = line.strip().split()
        l = int(tokens[0])
        r = int(tokens[1])
        left.append(l)
        right[r] = right[r] + 1

    result = 0
    for indx, v in enumerate(left):
        if v in right:
            result += v * right[v]
    
    print("Total similarity score = ", result)
    return 

if __name__ == "__main__":
    main()