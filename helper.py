import re

pattern = re.compile(r"^\d+,\d+,(NORTH|EAST|WEST|SOUTH)$")


class CommandError(Exception):
    """Raised when an invalid command is given"""
    pass


class PlaceCommandError(Exception):
    """Raised when an invalid command is given"""
    pass


def line_parser(line):
    values = line.strip().split()

    if not values:
        raise CommandError

    command = values[0]

    if command not in {"EXIT", "PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"}:
        raise CommandError

    coordinates = None
    if command == "PLACE":
        if len(values) != 2:
            raise PlaceCommandError

        valid = pattern.match(values[1])

        if not valid:
            raise PlaceCommandError
        arguments = values[1].split(',')

        coordinates = int(arguments[0]), int(arguments[1]), arguments[2]

    else:
        # PLACE is the only command that should have extra params
        if len(values) >= 2:
            raise CommandError

    return command, coordinates
