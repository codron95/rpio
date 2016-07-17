from gpio_module  import digitalReadChange
import time

def prin(x):
	print(str(x)+":state change on background thread")

digitalReadChange(8,prin)
while 1:
	print("Main thread")
	time.sleep(1)
