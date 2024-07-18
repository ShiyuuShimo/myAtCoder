s = list(input())
s.reverse()

while True:
	if s == []:
		print('YES')
		break
	elif ''.join(s[0:5]) == 'maerd':
		del s[0:5]
		continue
	elif ''.join(s[0:5]) == 'esare':
		del s[0:5]
		continue
	elif ''.join(s[0:6]) == 'resare':
		del s[0:6]
		continue
	elif ''.join(s[0:7]) == 'remaerd':
		del s[0:7]
		continue
	else:
		print('NO')
		break
