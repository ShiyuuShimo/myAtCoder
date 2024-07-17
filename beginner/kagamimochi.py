n = int(input())

list_input = []

for i in range(n):
	list_input.append(int(input()))

print(len(set(list_input)))