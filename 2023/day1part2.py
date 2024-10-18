# The numbers in each line can now be a spelled out numbers instead of digit.
# Big simplification: this code did not handle eleven, twelve, thirteen, ... , twenty, ... hundred 

DIGIT_MAP = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}
 
def findFirstNumber(line, digitMap):

    for index, c in enumerate(line):
        if c.isnumeric():
            return int(c)
        else:
            for digitStr in digitMap:
                if line.startswith(digitStr, index):
                    return digitMap[digitStr]
    return 0



def main():

    f = open('day1part1.dat', 'r')

    DIGIT_MAP_REVERSED = {}
    for (k, v) in DIGIT_MAP.items():
        DIGIT_MAP_REVERSED["".join(reversed(k))] = v
        
    sum = 0
    for line in f:

        # find first number
        sum += findFirstNumber(line, DIGIT_MAP) * 10

        # find last number
        lineR = "".join(reversed(line))
        sum += findFirstNumber(lineR, DIGIT_MAP_REVERSED)

    print("Total sum = {}".format(sum))

main()