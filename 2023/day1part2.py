# The numbers in each line can now be a spelled out numbers instead of digit.
# Big simplification: this code did not handle eleve, twelve, thirtheen, ... , twenty, ... hundred 

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

def main():

    sum = 0

    f = open('day1part1.dat', 'r')
    for line in f:

        num = 0

        # find first number
        for index, c in enumerate(line):
            if c.isnumeric():
                num += int(c) * 10
                break
            else:
                foundDigit = False
                for digitStr in DIGIT_MAP:
                    if line.startswith(digitStr, index):
                        num += DIGIT_MAP[digitStr]*10
                        foundDigit = True
                        break 
                if foundDigit:
                    break 

        # find last number
        lineR = "".join(reversed(line))
        for index, c in enumerate(lineR):
            if c.isnumeric():
                num += int(c)
                break
            else:
                foundDigit = False
                for digitStr in DIGIT_MAP:
                    digitStrR = "".join(reversed(digitStr))
                    if lineR.startswith(digitStrR, index):
                        num += DIGIT_MAP[digitStr]
                        foundDigit = True
                        break
                if foundDigit:
                    break

        print("line = {} num = {} ".format(line, num))
        sum += num
    print("Total sum = {}".format(sum))

main()