words = raw_input() 

num = int(words)

print "I hate",
for x in range(1,num):
	if x % 2 == 1:
		print "that I love",
	else:
		print "that I hate",
print "it"

