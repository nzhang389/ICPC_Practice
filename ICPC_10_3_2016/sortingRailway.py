# 1 3 5 2 4

# [3, 5, 6]
# [2, 2, 1]

from sys import stdin, stdout
n = map( int, stdin.readline().rstrip().split() )
cars = map(int, stdin.readline().rstrip().split())

lookingFor = {}
for c in cars:
	if c in lookingFor:
		lookingFor[c+1] = lookingFor[c] + 1
		lookingFor.pop(c)
	else:
		lookingFor[c+1] = 1

print n[0] - lookingFor[max(lookingFor, key = lambda i:lookingFor[i])]
