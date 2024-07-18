import sys

list_input = [int(x) for x in input().split(' ')]

for i in range(list_input[0]+1):
	for j in range(list_input[0]+1):
		if i+j <= list_input[0]:
			k = list_input[0] - i - j
			if 10000*i + 5000*j + 1000*k == list_input[1]:
				print(f'{i} {j} {k}')
				sys.exit()
else:
	print('-1 -1 -1')