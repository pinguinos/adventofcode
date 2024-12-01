def main():

    f = open('inputs/day1.dat', 'r')
    left = list()
    right = list()

    for line in f:
        tokens = line.strip().split()
        left.append(tokens[0])
        right.append(tokens[1])
    
    left.sort()
    right.sort()

    totalDiff = 0
    for indx, v in enumerate(left):
        totalDiff += abs(int(left[indx]) - int(right[indx]))
    
    print("Total difference = ", totalDiff)
    return


if __name__ == "__main__":
    main()