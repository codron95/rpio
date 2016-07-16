from gpio_module import log_pin
import time

log_pin(8)

while 1:
	print("Main thread")
	time.sleep(1)
