from gpio_module import digital_read,log_pin,state_callback
import time

def prin(x):
	print(str(x)+":state change on background thread")

state_callback(8,prin)
while 1:
	print("Main thread")
	time.sleep(1)
