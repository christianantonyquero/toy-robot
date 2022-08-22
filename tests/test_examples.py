"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""
from robot import Direction, Robot


class TestExamples:
    """
    A class that represent the testing for this solution
    """
    def test_memento(self, board, capsys):
        expected_output = "0,0,NORTH\n"

        robot = Robot(0, 0, Direction["NORTH"].value, board)
        board.place(robot)
        robot.report()

        actual, err = capsys.readouterr()
        assert expected_output == actual

    def test_a(self, board, capsys):
        expected_output = "0,1,NORTH\n"

        # SCENARIO:
        # PLACE
        # 0, 0, NORTH
        # MOVE
        # REPORT

        robot = Robot(0, 0, Direction["NORTH"].value, board)
        board.place(robot)
        robot.move()
        robot.report()

        actual, err = capsys.readouterr()
        assert expected_output == actual

    def test_b(self, board, capsys):
        expected_output = "0,0,WEST\n"

        # SCENARIO:
        # PLACE
        # 0, 0, NORTH
        # LEFT
        # REPORT

        robot = Robot(0, 0, Direction["NORTH"].value, board)
        board.place(robot)
        robot.left()
        robot.report()

        actual, err = capsys.readouterr()
        assert expected_output == actual

    def test_c(self, board, capsys):
        expected_output = "3,3,NORTH\n"

        # SCENARIO:
        # PLACE
        # 1, 2, EAST
        # MOVE
        # MOVE
        # LEFT
        # MOVE
        # REPORT

        robot = Robot(1, 2, Direction["EAST"].value, board)
        board.place(robot)
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        robot.report()

        actual, err = capsys.readouterr()
        assert expected_output == actual

    def test_go_beyond(self, board, capsys):
        expected_output = "4,2,EAST\n"

        # SCENARIO:
        # PLACE
        # 1, 2, EAST
        # MOVE
        # MOVE
        # MOVE
        # MOVE
        # MOVE
        # MOVE
        # REPORT

        robot = Robot(1, 2, Direction["EAST"].value, board)
        board.place(robot)
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.move()
        robot.report()

        actual, err = capsys.readouterr()
        assert expected_output == actual

    def test_place_multiple_robot_handle_only_one(self, board, capsys):
        expected_output = "3,3,NORTH\n"

        # SCENARIO:
        # PLACE
        # 1, 2, EAST
        # MOVE
        # MOVE
        # LEFT
        # MOVE
        # REPORT

        robot1 = Robot(1, 2, Direction["EAST"].value, board)
        robot2 = Robot(1, 2, Direction["EAST"].value, board)
        board.place(robot1)
        board.place(robot2)
        assert robot1 != robot2
        robot = board.get_robot()
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        robot.report()

        actual, err = capsys.readouterr()
        assert expected_output == actual
