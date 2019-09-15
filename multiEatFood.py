from pyautogui import click
import time

import configs

def MultiEatFood():
	while True:
		if configs.runProgram:
			click(button = 'right', x=1771, y=543)
			click(button = 'right', x=1771, y=543)
			time.sleep(2)
			click(button = 'right', x=3688, y=543)
			click(button = 'right', x=3688, y=543)

			time.sleep(5)
		else:
			time.sleep(5)


if __name__ == '__main__':
	MultiEatFood()