import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = sys.stdin.readline()
penguins = {"Emperor":0, "Macaroni":0,"Little":0}
for i in range(int(n)):
	penguin = sys.stdin.readline().rstrip().split()
	if penguin[0][0] == 'E':
		penguins["Emperor"] = penguins["Emperor"] + 1
	elif(penguin[0][0] == "M"):
		penguins["Macaroni"] = penguins["Macaroni"] + 1
	elif(penguin[0][0] == "L"):
		penguins["Little"] = penguins["Little"] + 1

print max(penguins, key = lambda i:penguins[i]) + " Penguin"