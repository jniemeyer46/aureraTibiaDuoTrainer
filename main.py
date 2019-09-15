from checkButtonPress import CheckButtonPress
from checkTime import CheckTime
from multiTrainMagicLevel import MultiTrainMagicLevel
from multiAntiIdle import MultiAntiIdle
from multiEatFood import MultiEatFood
from multiLogin import MultiLoginAndSetup
import configs

from pynput import keyboard
import threading
import time


''' Thread Class Definition '''
class myThread(threading.Thread):
	def __init__(self, ThreadID, ThreadName, ThreadAction):
		threading.Thread.__init__(self)
		self.ThreadID = ThreadID
		self.ThreadName = ThreadName
		self.ThreadAction = ThreadAction

	def run(self):
		print("Spinning up a thread for the " + self.ThreadName + " bot functionality.")
		self.ThreadAction()


def main():
	# Define the possible actions
	threadNames = ['Check-button-press', 'Check-Time', 'Multi-Anti-Idle', 'Multi-Eat-Food', 'Multi-Train-Magic-Level']
	threadActions = [CheckButtonPress, CheckTime, MultiAntiIdle, MultiEatFood, MultiTrainMagicLevel]
	threads = []
	threadID = 0

	for tName in threadNames:
		thread = myThread(threadID, tName, threadActions[threadID])
		thread.start()
		threads.append(thread)
		threadID += 1


if __name__ == '__main__':
	main()