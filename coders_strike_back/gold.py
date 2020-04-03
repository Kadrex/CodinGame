import math, sys


class Robot:

    def __init__(self):
        self.laps = 0
        self.checkpoint_count = 0
        self.checkpoints = []
        self.my_x = 0
        self.my_y = 0
        self.my_previous_x = 0
        self.my_previous_y = 0
        self.speed_vector_x = 0
        self.speed_vector_y = 0
        self.checkpoint_x = 0
        self.checkpoint_y = 0
        self.checkpoint_distance = 0
        self.checkpoint_angle = 0
        self.thrust = 100
        self.previous_checkpoint_distance = 0
        self.aim_x = 0
        self.aim_y = 0
        self.next_checkpoint_id = 0

    def my_distance_to_checkpoint(self):
        return math.sqrt(abs(self.my_x - self.checkpoint_x) ** 2 + abs(self.my_y - self.checkpoint_y) ** 2)

    def print_data(self):
        print("Angle... " + str(self.checkpoint_angle), file=sys.stderr)
        print("Speed vectors: " + str(self.speed_vector_x) + "; " + str(self.speed_vector_y), file=sys.stderr)
        print("Distance to checkpoint: " + str(self.checkpoint_distance), file=sys.stderr)
        print("Distance before: " + str(self.previous_checkpoint_distance) + "\nDistance now: " + str(self.checkpoint_distance), file=sys.stderr)
        print("Difference: " + str(self.previous_checkpoint_distance - self.checkpoint_distance), file=sys.stderr)
        print("Checkpoint coordinates: " + str(self.checkpoint_x) + " " + str(self.checkpoint_y), file=sys.stderr)

    def plan(self):
        self.checkpoint_distance = self.my_distance_to_checkpoint()
        self.aim_x = self.checkpoints[self.next_checkpoint_id][0]
        self.aim_y = self.checkpoints[self.next_checkpoint_id][1]
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

    def act(self):
        print(self.aim_x, self.aim_y, self.thrust)


class Data:

    def __init__(self, robot1: Robot, robot2: Robot):
        self.robot1 = robot1
        self.robot2 = robot2
        self.laps = int(input())
        self.checkpoint_count = int(input())
        self.checkpoints = []
        for i in range(self.checkpoint_count):
            checkpoint = [int(j) for j in input().split()]
            self.checkpoints.append(checkpoint)
        self.robot1.checkpoints = self.checkpoints
        self.robot2.checkpoints = self.checkpoints

    def sense(self):
        self.robot1.my_x, self.robot1.my_y, self.robot1.speed_vector_x, \
            self.robot1.speed_vector_y, self.robot1.checkpoint_angle, \
            self.robot1.next_checkpoint_id = [int(i) for i in input().split()]

        self.robot2.my_x, self.robot2.my_y, self.robot2.speed_vector_x, \
            self.robot2.speed_vector_y, self.robot2.checkpoint_angle, \
            self.robot2.next_checkpoint_id = [int(i) for i in input().split()]
        input()
        input()


if __name__ == '__main__':
    robot1 = Robot()
    robot2 = Robot()
    data = Data(robot1, robot2)
    while True:
        data.sense()
        robot1.print_data()
        robot1.plan()
        robot1.act()
        robot2.print_data()
        robot2.plan()
        robot2.act()
