import gpio_module as gpio
import time

t = gpio.digitalReadWithInterrupt(10)

t.start()
t.start()
while 1:
	time.sleep(4)
	print("Main thread Running")
	t.stop()
