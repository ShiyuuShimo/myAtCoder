list_input = [int(i) for i in input().split(' ')]

list_member = []

for j in range(list_input[0]+1):
	l = sum([int(k) for k in str(j)])
	if list_input[1] <= l and l <= list_input[2]:
		list_member.append(j)

print(sum(list_member))