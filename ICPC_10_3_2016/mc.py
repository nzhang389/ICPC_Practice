from sys import stdin, stdout
numBells, boxes = map( int, stdin.readline().rstrip().split() )
cowbells = map( int, stdin.readline().rstrip().split())

extraSpots = boxes * 2 - numBells
maxNum = 0

for x in range(0,(numBells - extraSpots)//2):
	val = cowbells[x] + cowbells[numBells - 1  - extraSpots - x]
	if val > maxNum:
		maxNum = val
if numBells == boxes * 2:
	print maxNum
else:
	maxNum = max(cowbells[len(cowbells)-1],maxNum)
	print maxNum