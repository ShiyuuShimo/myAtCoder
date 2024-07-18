v = [[int(i) for i in input().split()] for j in range(3)]

ab_sq = (v[1][0]- v[0][0])**2 + (v[1][1]- v[0][1])**2
bc_sq = (v[2][0]- v[1][0])**2 + (v[2][1]- v[1][1])**2
ca_sq = (v[0][0]- v[2][0])**2 + (v[0][1]- v[2][1])**2

if ab_sq + bc_sq == ca_sq:
	print('Yes')
elif bc_sq + ca_sq == ab_sq:
	print('Yes')
elif ca_sq + ab_sq == bc_sq:
	print('Yes')
else:
	print('No')