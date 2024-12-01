def main():

    time, distance = get_time_distance_from_input()
    count = num_beat_record( (time, distance) )

    print("Result = ", count)
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
    time = ''.join(lines[0].strip().split()[1:])
    distance = ''.join(lines[1].strip().split()[1:])
    return int(time), int(distance)


if __name__ == "__main__":
    main()