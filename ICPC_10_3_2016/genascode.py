import sys
from sys import stdin, stdout

n = map( int, stdin.readline().rstrip().split() )
countries = stdin.readline().rstrip().split()

nonbeautiful = "1"
numZeroes = 0
for country in countries:
	if country == "0":
		print 0
		sys.exit(0)
	if country[0] == "1":
		country = country[1:]
		if country == "" or int (country) == 0:
			numZeroes += len(country)
		else:
			nonbeautiful = "1" + country
	else:
		nonbeautiful = country


print( nonbeautiful + ("0" * numZeroes))


