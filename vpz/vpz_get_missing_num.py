def getNo(no):
	for i in range(len(no)-1):
		if(no[i+1] - no [i]> 1):
			print(no[i]+1)


def getNo2(no):
	n=no[len(no)-1]
	tsum=n*(n+1)/2
	sm=sum(no)
	print(tsum-sm)

dt =list(range(1420))
dt.remove(1124)

getNo(dt)
getNo2(dt)