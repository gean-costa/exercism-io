import random
import string


class Robot:
    robot_names = []
    name = ''

    def __init__(self):

        # first letter
        self.name = random.choice(string.ascii_uppercase)
        # second letter
        self.name += random.choice(string.ascii_uppercase)
        # first number
        self.name += str(random.choice(range(0, 10)))
        # second number
        self.name += str(random.choice(range(0, 10)))
        # third number
        self.name += str(random.choice(range(0, 10)))

        if self.name not in self.robot_names:
            self.robot_names.append(self.name)
        else:
            self.reset()

    def reset(self):
        self.__init__()
