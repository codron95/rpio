from gpio_module import digitalReadWithInterrupt
import time

t = digitalReadWithInterrupt(10,True)

t.start()
t.start()
while 1:
	time.sleep(4)
	print("Main thread Running")
	t.stop()
