import sys

n = int(input())
list_int = [int(i) for i in input().split(' ')]
c = 0

while True:
	for l in range(n):
		if list_int[l] % 2 == 0:
			list_int[l] = list_int[l] / 2
		else:
			print(c)
			sys.exit()
	c += 1
