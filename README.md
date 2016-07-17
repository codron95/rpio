# rpio
A library to read raspberry pi gpio, log states and provide callbacks on state changes

This library provides you with 3 functions
1) digital read the rpi gpio pin
2) log the state of a pin to a file on a separate thread
3) call a function that you pass as a parameter when the state of the pin changes

Separate threads run as long as the main or host threads run

1) digitalRead(pin,mode)
pin -> pin you want to read
mode-> scheme of board numbering you want to use, GPIO.BOARD by default

2) digitalReadLog(pin,filename,freq,mode)
pin and mode same as digital_read
filename->name of the log file created. log.txt by default
freq-> frequency at which the logging takes place, 1s by default

3) digitalReadChange(pin,callback,freq,mode)
pin,freq and mode as previous
callback -> function call that you provide. must contain one argument which will contain the 
current state as the state changes

4) For interrupt capability to stop logging on main thread, use class digitalReadWithInterrupt
Code example:-logging_interrupt.py

<--View code examples digitalread.py, callback.py, logging.py for understanding usage further -->
