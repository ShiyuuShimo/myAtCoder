n, k, x = map(int, input().split())
a = [int(i) for i in input().split(' ')]

a.insert(k, x)
b = ''

for j in range(len(a)):
	b = f'{b}{a[j]} '

print(b.rstrip())