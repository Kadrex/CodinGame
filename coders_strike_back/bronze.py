import sys
import math


class Robot:

    def __init__(self):
        self.my_x = 0
        self.my_y = 0
        self.opponent_x = 0
        self.opponent_y = 0
        self.checkpoint_x = 0
        self.checkpoint_y = 0
        self.checkpoint_distance = 0
        self.checkpoint_angle = 0
        self.thrust = 100

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

    def plan(self):
        self.thrust = "BOOST"
        if self.checkpoint_angle > 100 or self.checkpoint_angle < -100:
            self.thrust = 15
        elif self.checkpoint_distance < 1000:
            self.thrust = 80

    def act(self):
        print(self.checkpoint_x, self.checkpoint_y, self.thrust)


if __name__ == '__main__':
    robot = Robot()
    while True:
        robot.sense()
        robot.print_data()
        robot.plan()
        robot.act()
