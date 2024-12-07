def main():

    f = open('inputs/day4.dat', 'r')
    lines = [line.strip() for line in f]
    xlimit = len(lines[0])
    ylimit = len(lines)

    count = 0
    for i in range(0, xlimit, 1):
        for j in range(0, ylimit, 1):

            if lines[i][j] != 'A':
                continue

            if (i-1) < 0 or (i+1) >= xlimit \
                or (j-1) < 0 or (j+1) >= ylimit:
                continue

            forwardX = ( lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M' ) \
                    or ( lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S')
            
            backwardX = ( lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M') \
                     or ( lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S')
            
            if not forwardX or not backwardX:
                continue

            count += 1
    
    print("Result = ", count)
    return

if __name__ == '__main__':
    main()