def factTwo(no):
	c=1
	for x in range(no):
		c=c+c*x
	print(c)
	t=c%100
	if t==0:
		print("00")
	else:
		print(t)

factTwo(12)