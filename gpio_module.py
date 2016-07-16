import RPi.GPIO as GPIO
import time
import threading

def digital_read(pin,mode=GPIO.BOARD):
	if(pin==None):
		print("Please specify the pin no.")
		return
	else:
		GPIO.setmode(mode)
		GPIO.setup(pin,GPIO.IN)
		return GPIO.input(pin)

def file_log(pin,filename="log.txt",freq=1,mode=GPIO.BOARD):
	if(pin==None):
		print("Please specify the pin no.")
		return
	else:
		GPIO.setmode(mode)
		GPIO.setup(pin,GPIO.IN)
		file=open(filename,"w+")
		while 1:
			state=GPIO.input(pin)
			cur_time=time.asctime(time.localtime(time.time()))
			log=cur_time+"\t\t"+str(state)+"\n"
			print(log)
			file.write(log)
			time.sleep(freq)

def state_change_callback(pin,callback,freq=1,mode=GPIO.BOARD):
	if(pin==None):
		print("Please specify the pin no")
	else:
		GPIO.setmode(mode)
		GPIO.setup(pin,GPIO.IN)
		prev=GPIO.input(pin)
		time.sleep(freq)
		while 1:
			next=GPIO.input(pin)
			if next!=prev:
				callback(next)
			prev=next
			time.sleep(freq)

def log_pin(pin,filename="log.txt",freq=1,mode=GPIO.BOARD):
	thread=threading.Thread(target=file_log,args=(pin,filename,freq,mode,))
	thread.daemon=True
	thread.start()

def state_callback(pin,callback,freq=1,mode=GPIO.BOARD):
	thread=threading.Thread(target=state_change_callback,args=(pin,callback,freq,mode,))
	thread.daemon=True
	thread.start()