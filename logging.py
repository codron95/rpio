from gpio_module import digitalReadLog
import time

digitalReadLog(8)

while 1:
	print("Main thread")
	time.sleep(1)
