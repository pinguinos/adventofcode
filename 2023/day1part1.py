# Give a list of strings, find the first and last occurring digit in each string, collapse the two digits into a single two-digit number 
# and sum across all lines in the input file.

def main():

    f = open('input/day1part1.dat', 'r')
    sum = 0
    for line in f:
        
        num = 0

        # find first occurring digit
        for c in line:
            if c.isnumeric():
                num += int(c)*10
                break
        
        # find last occurring digit by reverse string
        for c in reversed(line):
            if c.isnumeric():
                num += int(c)
                break
        
        sum += num

    print("Total sum = {}".format(sum))
    return

main()