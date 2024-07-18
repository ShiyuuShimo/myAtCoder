keys = ['Red', 'Green', 'Blue']
input_list = [int(i) for i in input().split(' ')]
c = input()

target = [(v, k) for v, k in zip(input_list, keys) if k != c]
target.sort()

print(target[0][0])
