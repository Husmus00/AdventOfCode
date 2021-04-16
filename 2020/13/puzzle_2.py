with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    earliest = int(lines[0])
    ids = [item for item in lines[1].split(',')]

print(ids)

multiple = 1
timestamps = [' '] * len(ids)
succeeded = False

while not succeeded:
    print(multiple)
    for i in range(0, len(ids) + 1):
        if i == len(ids):
            succeeded = True
            break

        if i == 0:
            timestamps[0] = int(ids[0]) * multiple
            continue
        elif ids[i] == 'x':
            timestamps[i] = 'x'
            continue

        ts = ids[i] * multiple
        if ts == timestamps[0] + i:
            continue
        else:
            multiple += 1
            break


min_waiting_time = min(timestamps) - earliest
earliest_id = ids[timestamps.index(min(timestamps))]
print("Earliest possible stop is bus {0} with a waiting time of {1}".format(earliest_id, min_waiting_time))
print(earliest_id * min_waiting_time)
