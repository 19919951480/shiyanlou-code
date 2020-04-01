count =1
while count <= 100:
	flag = 0
	if count % 7 == 0:
		flag =1
	else:
		temp = count
		while temp > 0:
			if temp % 10 == 7:
				flag = 1
			temp = temp // 10
	if flag != 1:
		print(count)
	count += 1
