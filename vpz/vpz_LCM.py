def LCM(n1,n2):
	print(n1,n2)
	for x in range(1,n1*n2):
		if (n1*n2)%x ==0:
			return x

print("LCM: ", LCM(12,6))
	