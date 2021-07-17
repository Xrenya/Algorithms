with open('input.txt') as f:
    students, teachers = list(map(int, f.readline().split()))
    events = []
    for _ in range(teachers):
        start, end = list(map(int, f.readline().split()))
        events.append((start, -1))
        events.append((end, 1))
    events.sort()

def leftstudents(students, teachers, events):
    cnt = 0
    watchers = 0
    for i in range(len(events)):
        if watchers > 0:
            cnt += events[i][0] - events[i-1][0]
        if events[i][1] == -1:
            watchers += 1
        else:
            watchers -= 1
        if watchers == 0:
            cnt += 1
    return students - cnt

if __name__ == '__main__':
    left = leftstudents(students, teachers, events)
    with open('output.txt', 'w') as file:
        file.write(f"{left}")
