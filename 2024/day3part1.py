import re

def main():

    f = open('inputs/day3.dat', 'r')
    lines = f.readlines()

    sum = 0
    for line in lines:
        sum += get_line_sum(line)

    print("Result = ", sum)
    return 

def get_line_sum(line):

    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line.strip())
    lineSumList = [int(num1)*int(num2) for num1, num2 in matches]
    lineSum = sum(lineSumList)
    return lineSum


if __name__ == "__main__":
    main()