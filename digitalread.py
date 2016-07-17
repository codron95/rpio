from gpio_module import digitalRead
import time

while 1:
	print(digitalRead(8))
	time.sleep(1)
