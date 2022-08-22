#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Christian Antony Quero"
__version__ = "0.1.0"
__license__ = "MIT"

import fileinput

from board import Board
from helper import line_parser, CommandError, PlaceCommandError
from robot import Direction, Robot


def main():
    """ Main entry point of the app """
    board = Board()
    # invoker = Invoker(board)

    for line in fileinput.input():
        try:
            command_string, coordinates = line_parser(line)

            if command_string == "EXIT":
                exit()

            if command_string == "PLACE":
                # Currently, if you trigger this more than once.
                # It will create a new robot and replace the older robot on the robo_map
                robot = Robot(coordinates[0], coordinates[1], Direction[coordinates[2]].value, board)
                board.place(robot)
            else:
                if board.robo_map:
                    robot_receiver = board.get_robot()
                    function = getattr(robot_receiver, command_string.lower())
                    function()

        except CommandError:
            print(CommandError, "error trying the command you entered")
        except PlaceCommandError:
            print(PlaceCommandError, "error trying the PLACE command you entered")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
