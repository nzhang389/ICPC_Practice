from sys import stdin, stdout
length, start = map( int, stdin.readline().rstrip().split() )
cityMap = map( int, stdin.readline().rstrip().split())

totalCrim = 0
for x in range(length):
	a = start - x - 1
	b = start + x - 1
	if a < 0 and b > length-1:
		break
	elif a < 0:
		if(cityMap[b] == 1):
			totalCrim = totalCrim+1
	elif b > length -1:
		if cityMap[a] == 1:
			totalCrim=totalCrim+1
	else:
		if(cityMap[a] and cityMap[b]):
			if a ==b:
				totalCrim = totalCrim + 1
			else:
				totalCrim = totalCrim + 2

print totalCrim
