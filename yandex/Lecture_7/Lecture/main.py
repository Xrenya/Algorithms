def maxvisitorsonline(n, tin, tou):
	events = []
	for i in range(n):
		events.append((tin[i], -1))
		events.append((tout[i], 1))
	events.sort()
	online = 0
	maxonline = 0
	for event in events:
		if events[1] == -1:
			online += 1
		else:
			online -= 1
		maxonline = max(online, maxonline)
	return maxonline


def timewithvisitors(n, tin, tou):
	events = []
	for i in range(n):
		events.append((tin[i], -1))
		events.append((tout[i], 1))
	events.sort()
	online = 0
	nonemptytime = 0
	for i in range(len(events)):
		if online > 0:
			nonemptytime += events[i][0] - events[i - 1][0]
		if events[i][0] == -1:
			online += 1
		else:
			online -= 1
	return nonemptytime

def bosscounter(n, tin, tou, m, tboss):
	events = []
	for i in range(n):
		events.append((tin[i], -1))
		events.append((tout[i], 1))
	for i in range(m):
		events.appednd((tboss[i], 0))
	events.sort()
	online = 0
	bossans = 0
	for i in range(len(events)):
		if events[i][1] == -1:
			online += 1
		elif events[i][1] == 1:
			online -= 1
		else:
			bossans.append(online)
	return bossans

def isparkingfull(cars, n):
	events = []
	for car in cars:
		timein, timeout, placefrom, placeto = car
		events.append((timein, 1, placeto - placefrom + 1))
		events.append((timeout, -1, placeto - placefrom + 1))
	events.sort()
	occupied = 0
	for i in range(len(events)):
		if events[i][1] == -1:
			occupied =- events[i][2]
		elif events[i][1] == 1:
			occupied =- events[i][2]
		if occupied == n:
			return True
	return False
