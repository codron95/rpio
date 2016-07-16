from gpio_module import digital_read
import time

while 1:
	print(digital_read(8))
	time.sleep(1)
