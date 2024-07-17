n = input()
list_input = [int(i) for i in input().split(' ')]
list_input.sort(reverse=True)

list_alice = list_input[::2]
list_bob = list_input[1::2]

print(sum(list_alice)-sum(list_bob))
