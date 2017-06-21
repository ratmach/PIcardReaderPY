#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
from evdev import uinput, ecodes as e

letter_to_key = {
	"0":e.KEY_0,
	"1":e.KEY_1,
	"2":e.KEY_2,
	"3":e.KEY_3,
	"4":e.KEY_4,
	"5":e.KEY_5,
	"6":e.KEY_6,
	"7":e.KEY_7,
	"8":e.KEY_8,
	"9":e.KEY_9,
	"a":e.KEY_A,
	"b":e.KEY_B,
	"c":e.KEY_C,
	"d":e.KEY_D,
	"e":e.KEY_E,
	"f":e.KEY_F,
	"g":e.KEY_G,
	"h":e.KEY_H,
	"i":e.KEY_I,
	"j":e.KEY_J,
	"k":e.KEY_K,
	"l":e.KEY_L,
	"m":e.KEY_M,
	"n":e.KEY_N,
	"o":e.KEY_O,
	"p":e.KEY_P,
	"q":e.KEY_Q,
	"r":e.KEY_R,
	"s":e.KEY_S,
	"t":e.KEY_T,
	"u":e.KEY_U,
	"v":e.KEY_V,
	"w":e.KEY_W,
	"x":e.KEY_X,
	"y":e.KEY_Y,
	"z":e.KEY_Z,
	" ":e.KEY_SPACE,
	"\n":e.KEY_ENTER
}
def keysim_write(dump__):
	with uinput.UInput() as ui:
		for letter in dump__:
			tp = letter_to_key[letter.lower()]
			ui.write(e.EV_KEY, tp, 1)
			ui.write(e.EV_KEY, tp, 0)
			ui.syn()

continue_reading = True

def end_read(signal,frame):
	global continue_reading
	print "Ctrl+C captured, ending read."
	continue_reading = False
	GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()

while continue_reading:
	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	if status == MIFAREReader.MI_OK:
		print "Card detected"
	(status,uid) = MIFAREReader.MFRC522_Anticoll()
	if status == MIFAREReader.MI_OK:
		print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
		key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
		MIFAREReader.MFRC522_SelectTag(uid)
		status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
		if status == MIFAREReader.MI_OK:
			arr = MIFAREReader.MFRC522_Read(8)
			print(arr)
			keysim_write("".join(list(map(lambda x: str(x), arr))) + "\n")
			MIFAREReader.MFRC522_StopCrypto1()
		else:
			print "Authentication error"