

import gpiozero as zero
from gpiozero import LED
from gpiozero import Button
from time import sleep
import readline

butt1 = Button(25)
butt2 = Button(26)
led_set = [ 0 for x in range(25)]


for led_num in range(25):
	led_set[led_num] = LED(led_num)
	led_set[led_num].off()

def func1():
	for led_num in range(25):
		led_set[led_num].off()
def func2():
	for led_num in range(25):
		led_set[led_num].on()
butt1.when_pressed = func1
butt2.when_pressed = func2


sleep(5)
func2()
sleep(5)
func1()
sleep(5)
func2()
sleep(5)
func1()
