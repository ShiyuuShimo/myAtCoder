import sys

n = int(input())
input_list = [[int(i) for i in input().split()] for j in range(n)]

#元の地点からのマンハッタン距離における直線距離を算出し，最速でもその地点に到達できない場合を落とす
#元の地点からの偶奇を判定し，必要な移動回数の偶奇で判定する（偶数ならyes, 奇数ならno）

for k in range(len(input_list)):
	if k == 0:
		step = input_list[0][0]
		dist = abs(input_list[0][1]) + abs(input_list[0][2])
	else:
		step = input_list[k][0] - input_list[k-1][0]
		dist = abs(input_list[k][1] - input_list[k-1][1]) + abs(input_list[k][2] - input_list[k-1][2])
	
	diff = step - dist

	#各ステップで必要な移動量が可能な移動量より大きい場合を落とす
	if diff < 0:
		print('No')
		sys.exit()
	#可能な移動回数の偶奇を判定して奇数の場合を落とす
	elif diff % 2 == 1:
		print('No')
		sys.exit()
	#1回しか移動しない場合のみここで終了
	elif n == 1:
		break

print('Yes')
