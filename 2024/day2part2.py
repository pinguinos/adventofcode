def main():
    
    f = open('inputs/day2.dat', 'r')
    lines = f.readlines()

    count = 0
    for line in lines:
        tokens = line.strip().split()
        for i in range(0, len(tokens), 1):
            newTokens = tokens[:i] + tokens[i+1:] #remove element at index i
            if isSafe(newTokens):
                count += 1
                break

    print("Result count = ", count)
    return

def isSafe(tokens):

    for indx, v in enumerate(tokens):

        if (indx + 1) >= len(tokens):
            break

        diff = int(tokens[indx+1]) - int(tokens[indx])
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        
        if indx == 0:
            isIncreasing = (diff > 0)

        if ( isIncreasing and diff < 0 ) \
           or (not isIncreasing and diff > 0):
            return False
        
    return True


if __name__ == '__main__':
    main()