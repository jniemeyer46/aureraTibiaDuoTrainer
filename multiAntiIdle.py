from pyautogui import hotkey
import time
import random

import configs


def MultiAntiIdle():
	while True:
		if configs.runProgram:
			DirectionChoices = ['up', 'down', 'left', 'right']

			Direction = random.choice(DirectionChoices)

			hotkey('ctrl', Direction)

			time.sleep(1)
		else:
			time.sleep(5)


if __name__ == '__main__':
	MultiAntiIdle()