from gpio_module  import digitalReadChangeWithInterrupt
import time

def prin(x):
	print(str(x)+":state change on background thread")

t=digitalReadChangeWithInterrupt(8,prin)
t.start()
t.start()
while 1:
	print("Main thread Running")
	time.sleep(4)
	t.stop()
