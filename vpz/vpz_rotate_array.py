def rotateL(arr, n):
	for x in range(n):
		start=arr[0]
		for i in range(1,len(arr)):
			arr[i-1]=arr[i]
		arr[-1]=start

def rotateR(arr,n):
	for x in range(n):
		end=arr[-1]
		for i in range(len(arr)-1,-1,-1):
			arr[i]=arr[i-1]
		arr[0]=end

x=list(range(1,8))
print(x)
rotateL(x,2)
print(x)
rotateR(x,2)
print(x)