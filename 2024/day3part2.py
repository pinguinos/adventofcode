import re

def main():

    f = open('inputs/day3.dat', 'r')
    text = f.read()

    sum = 0
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    rawMatches = re.findall(pattern, text.strip())
    matches = filter_match(rawMatches)
    sum += compute_sum(matches)

    print("Result = ", sum)        
    return

def get_match_in_line(line):

    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, line.strip())
    return matches

def filter_match(rawMatches):

    filteredMatches = list()

    shouldInclude = True
    for v in rawMatches:

        if "mul" in v and shouldInclude:
            filteredMatches.append(v)
        if "do()" == v:
            shouldInclude = True
        if "don't()" == v:
            shouldInclude = False
    
    return filteredMatches

def compute_sum(matches):

    pattern = r"mul\((\d+),(\d+)\)"
    
    sum = 0
    for match in matches:
        matches = re.findall(pattern, match)
        num1 = int(matches[0][0])
        num2 = int(matches[0][1])
        sum +=  (num1 * num2) 

    return sum


if __name__ == "__main__":
    main()