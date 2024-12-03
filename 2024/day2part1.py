def main():
    
    f = open('inputs/day2.dat', 'r')
    lines = f.readlines()

    count = 0
    for line in lines:
        tokens = line.strip().split()
        if isSafe(tokens):
            count += 1
    print("Result count = ", count)
    return

def isSafe(tokens):

    for indx, v in enumerate(tokens):

        if (indx + 1) >= len(tokens):
            break

        diff = int(tokens[indx+1]) - int(tokens[indx])
        if diff == 0 or abs(diff) > 3 or abs(diff) < 1:
            return False
        
        if indx == 0:
            isIncreasing = (diff > 0)

        if ( isIncreasing and diff < 0 ) \
           or (not isIncreasing and diff > 0):
            return False
        
    return True


if __name__ == '__main__':
    main()