from pyautogui import hotkey
import time
import random

import configs


def MultiAntiIdle():
	while True:
		if configs.runProgram:
			Direction = 'up'

			hotkey(Direction)

			time.sleep(1)
		else:
			time.sleep(5)


if __name__ == '__main__':
	MultiAntiIdle()