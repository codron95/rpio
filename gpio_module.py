import RPi.GPIO as GPIO
import time
import threading

def digitalRead(pin,debug=1,mode=GPIO.BOARD):
	if(pin==None):
		if debug:
			print("Please specify the pin no. Error code 2")
		return 2
	else:
		GPIO.setmode(mode)
		GPIO.setup(pin,GPIO.IN)
		return GPIO.input(pin)

def file_log(pin,debug=1,filename="log.txt",freq=1,mode=GPIO.BOARD):
	if(pin==None):
		if debug:
			print("Please specify the pin no. Error code 2")
		return 2
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

def state_change_callback(pin,callback,debug=1,freq=1,mode=GPIO.BOARD):
	if(pin==None):
		if debug:
			print("Please specify the pin no. Error code 2")
		return 2
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

def digitalReadLog(pin,debug=1,filename="log.txt",freq=1,mode=GPIO.BOARD):
	thread=threading.Thread(target=file_log,args=(pin,debug,filename,freq,mode,))
	thread.daemon=True
	thread.start()

def digitalReadChange(pin,callback,debug=1,freq=1,mode=GPIO.BOARD):
	thread=threading.Thread(target=state_change_callback,args=(pin,callback,debug,freq,mode,))
	thread.daemon=True
	thread.start()
	
class digitalReadWithInterrupt(threading.Thread):
	def __init__(self,pin,debug=1,filename="log.txt",freq=1,mode=GPIO.BOARD):
		self.pin=pin
		self.control=0
		self.filename=filename
		self.freq=freq
		self.mode=mode
		self.debug=debug
		
	def file_log(self):
		if(self.pin==None):
			if self.debug:
				print("Please specify the pin no. Error code 2")
			return 2
		else:
			GPIO.setmode(self.mode)
			GPIO.setup(self.pin,GPIO.IN)
			file=open(self.filename,"w+")
			while self.control:
				state=GPIO.input(self.pin)
				cur_time=time.asctime(time.localtime(time.time()))
				log=cur_time+"\t\t"+str(state)+"\n"
				print(log)
				file.write(log)
				time.sleep(self.freq)
	
	def start(self):
		if not self.control:
			thread=threading.Thread(target=self.file_log,args=())
			thread.daemon=True
			thread.start()
			self.control=1
		else:
			if self.debug:
				print("thread already running on pin:"+str(self.pin)+" Error code 3")
			return 3
				
				
	def stop(self):
		if self.control:
			self.control=0
			print("terminating thread on pin:"+str(self.pin))
		else:
			if self.debug:
				print("No running thread. Error code 4")
			return 4
			
			
class digitalReadChangeWithInterrupt(threading.Thread):
	def __init__(self,pin,callback,debug=1,freq=1,mode=GPIO.BOARD):
		self.pin=pin
		self.control=0
		self.callback=callback
		self.freq=freq
		self.mode=mode
		self.debug=debug
		
	def state_change_callback(self):
	if(self.pin==None):
		if self.debug:
			print("Please specify the pin no. Error code 2")
		return 2
	else:
		GPIO.setmode(self.mode)
		GPIO.setup(self.pin,GPIO.IN)
		prev=GPIO.input(self.pin)
		time.sleep(self.freq)
		while 1:
			next=GPIO.input(self.pin)
			if next!=prev:
				callback(next)
			prev=next
			time.sleep(self.freq)
	
	def start(self):
		if not self.control:
			thread=threading.Thread(target=self.state_change_callback,args=())
			thread.daemon=True
			thread.start()
			self.control=1
		else:
			if self.debug:
				print("thread already running on pin:"+str(self.pin)+" Error code 3")
			return 3
				
				
	def stop(self):
		if self.control:
			self.control=0
			print("terminating thread on pin:"+str(self.pin))
		else:
			if self.debug:
				print("No running thread. Error code 4")
			return 4
		
		
