def main():

    timeDisPairs = get_time_distance_from_input()
    print(timeDisPairs)

    result = 1
    for tdpair in timeDisPairs:
        result = result * num_beat_record(tdpair)
    
    print("Result = ", result)
    return

def num_beat_record(tdpair):

    time = tdpair[0]
    distance = tdpair[1]
    count = 0
    
    for i in range (1, time+1, 1):
        if (time - i) * i > distance:
            count += 1
    
    return count

def get_time_distance_from_input():

    f = open('inputs/day6.dat', 'r')
    lines = f.readlines()
    times = lines[0].strip().split()
    distances = lines[1].strip().split()

    tuples = list()
    for indx, time in enumerate(times):
        if indx == 0:
            continue
        data = (int(time), int(distances[indx]))
        tuples.append(data)

    return tuples

if __name__ == "__main__":
    main()