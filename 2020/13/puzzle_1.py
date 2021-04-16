with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    earliest = int(lines[0])  # 'earliest timestamp you could depart on a bus.'
    ids = [int(item) for item in lines[1].split(',') if item != 'x']

timestamps = []

for i in range(0, len(ids)):
    ts = int(ids[i])
    # Keep increasing each id until it's greater than 'earliest' and add it to a separate list 'timestamps'
    while ts < earliest:
        ts += ids[i]
    timestamps.append(ts)

# Then find the minimum among these (the closest to the earliest timestamp)
min_waiting_time = min(timestamps) - earliest
earliest_id = ids[timestamps.index(min(timestamps))]
print("Earliest possible stop is bus {0} with a waiting time of {1}".format(earliest_id, min_waiting_time))
print(earliest_id * min_waiting_time)
