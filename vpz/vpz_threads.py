import threading
import time

def add_and_print(a, b):
    time.sleep(3)
    result = a + b
    print("result =", result)

threading.Thread(target=add_and_print,
                 args=(3, 5)
                 ).start()

print("finish")

def prnt(s1):
	for x in range(12):
		time.sleep(0.25)
		if x%2==0:
			print(s1+":", x)

args=["vinod"]
t1=threading.Thread(target=prnt,args=args)
args=["pawar"]
t2=threading.Thread(target=prnt,args=args)
t1.start()
t2.start()