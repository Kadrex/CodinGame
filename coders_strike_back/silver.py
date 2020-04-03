import math
import sys


class Robot:

    def __init__(self):
        self.my_x = 0
        self.my_y = 0
        self.my_previous_x = 0
        self.my_previous_y = 0
        self.opponent_x = 0
        self.opponent_y = 0
        self.opponent_previous_x = 0
        self.opponent_previous_y = 0
        self.checkpoint_x = 0
        self.checkpoint_y = 0
        self.checkpoint_distance = 0
        self.checkpoint_angle = 0
        self.thrust = 100
        self.previous_checkpoint_distance = 0
        self.aim_x = 0
        self.aim_y = 0

    def sense(self):
        self.my_x, self.my_y, self.checkpoint_x, self.checkpoint_y, \
            self.checkpoint_distance, self.checkpoint_angle = \
            [int(i) for i in input().split()]
        self.opponent_x, self.opponent_y = [int(i) for i in input().split()]

    def print_data(self):
        print("Angle... " + str(self.checkpoint_angle), file=sys.stderr)
        print("Distance to checkpoint: " + str(self.checkpoint_distance), file=sys.stderr)
        print("Distance between me and opponent: "
              + str(math.sqrt(abs(self.my_x - self.opponent_x) ** 2 + abs(self.my_y - self.opponent_y) ** 2)),
              file=sys.stderr)
        print("Distance before: " + str(self.previous_checkpoint_distance) + "\nDistance now: " + str(self.checkpoint_distance), file=sys.stderr)
        print("Difference: " + str(self.previous_checkpoint_distance - self.checkpoint_distance), file=sys.stderr)
        print("Checkpoint coordinates: " + str(self.checkpoint_x) + " " + str(self.checkpoint_y), file=sys.stderr)

    def plan(self):
        self.aim_x = self.checkpoint_x
        self.aim_y = self.checkpoint_y
        self.thrust = 100
        if self.previous_checkpoint_distance > 0:
            self.aim_x += self.my_previous_x - self.my_x
            self.aim_y += self.my_previous_y - self.my_y
        if self.checkpoint_angle > 100 or self.checkpoint_angle < -100:
            self.thrust = 15
            if self.checkpoint_distance < 1780:
                self.thrust = 5
        elif self.checkpoint_distance < 1500:
            self.thrust = 80
        elif self.checkpoint_distance > 3700:
            self.thrust = "BOOST"
        self.previous_checkpoint_distance = self.checkpoint_distance
        self.my_previous_x = self.my_x
        self.my_previous_y = self.my_y
        self.opponent_previous_x = self.opponent_x
        self.opponent_previous_y = self.opponent_y

    def act(self):
        print(self.aim_x, self.aim_y, self.thrust)


if __name__ == '__main__':
    robot = Robot()
    while True:
        robot.sense()
        robot.print_data()
        robot.plan()
        robot.act()
