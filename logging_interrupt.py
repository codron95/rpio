from gpio_module import digitalReadWithInterrupt
import time

t = digitalReadWithInterrupt(10)

t.start()
while 1:
	time.sleep(4)
	print("Main thread Running")
	t.stop()
