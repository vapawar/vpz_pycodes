def bubble_sort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

def lnr_search(nums, x):
	for i in range(len(nums)):
		if nums[i]==x:
			return i
	return -1

def bnr_search(nums, n):
	start=0
	end=len(nums)-1
	m=(start+end)//2
	while start<=end:
		if nums[m]<n:
			start=m+1
		if nums[m]>n:
			end=m-1
		if nums[m]==n:
			return m
		m=(start+end)//2
	return -1

x=[39,48,4,9,74,24,85,25,58,47,96]
print("before sort",x)
print("bubble sort",bubble_sort(x))
from datetime import datetime
print(datetime.now())
print("lnsearch:",lnr_search(x,24))
print (datetime.now())
print("bnsearch:",bnr_search(x,24))
print( datetime.now())