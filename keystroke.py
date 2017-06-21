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