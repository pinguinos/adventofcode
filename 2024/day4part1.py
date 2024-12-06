def main():

    match = 'XMAS'

    f = open('inputs/day4.dat', 'r')
    lines = [line.strip() for line in f]
    xlen = len(lines[0])
    ylen = len(lines)
    print(xlen)
    print(ylen)

    matchCount = 0
    for i in range(0, xlen, 1):
        for j in range(0, ylen, 1):
            for lr in range(-1, 2, 1):
                for up in range(-1, 2, 1):

                    isMatch = True
                    for offset in range(0, len(match), 1):
                        x = i + lr * offset
                        y = j + up * offset
                        if x < 0 or x >= xlen or y < 0 or y >= ylen or lines[x][y] != match[offset]:
                            isMatch = False
                            break
                    
                    if isMatch:
                        matchCount += 1
    
    print("Result = ", matchCount)
    return
                    
if __name__ == "__main__":
    main()