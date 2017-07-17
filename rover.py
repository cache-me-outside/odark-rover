from rrb3 import *
import time

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

DISTANCE_THRESHOLD = 20


class Rover(object):
	def __init__(self):
		self.rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

	def run_autonomous(self):
		while True:
			distance = self.rr.get_distance()

			if distance < DISTANCE_THRESHOLD:
				self.turn_right()
			else:
				self.rr.forward()

	def turn_right(self):
		self.rr.set_motors(0.5, 0, 0.5, 1)
		time.sleep(1.4)
		self.rr.stop()

	def __del__(self):
		self.rr.stop()
		self.rr.cleanup()

if __name__ == "__main__":
	rover = Rover()
	rover.run_autonomous()
