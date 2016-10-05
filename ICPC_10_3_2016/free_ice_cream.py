# free ice cream

# sortedWords = words.split()
# nums = words.split(" ")
# ice = nums[0]
# kids = nums[1]


# print nums

from sys import stdin, stdout
kids, ice = map( int, stdin.readline().rstrip().split() )
operations = [[0 for x in range(2)] for y in range(kids)] 
for x in range(kids):
	operations[x] = map(str, stdin.readline().rstrip().split())

sadKids = 0
for op in operations:
	if op[0] == "+":
		ice += int(op[1])
	else:
		iceToLose = int(op[1])
		if ice - iceToLose < 0:
			sadKids = sadKids + 1
		else:
			ice = ice - iceToLose

print ice, sadKids