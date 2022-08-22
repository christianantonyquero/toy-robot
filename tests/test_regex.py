import pytest

from helper import line_parser, CommandError, PlaceCommandError


class Test:
    def test_valid_exit(self):
        command, param = line_parser("EXIT")
        assert param is None
        assert command == "EXIT"

    def test_valid_place(self):
        command, coordinates = line_parser("PLACE 0,0,NORTH")
        assert command == "PLACE"
        assert coordinates[0] == 0
        assert coordinates[1] == 0
        assert coordinates[2] == "NORTH"

    def test_valid_move(self):
        command, param = line_parser("MOVE")
        assert param is None
        assert command == "MOVE"

    def test_valid_left(self):
        command, param = line_parser("LEFT")
        assert param is None
        assert command == "LEFT"

    def test_valid_right(self):
        command, param = line_parser("RIGHT")
        assert param is None
        assert command == "RIGHT"

    def test_valid_report(self):
        command, param = line_parser("REPORT")
        assert param is None
        assert command == "REPORT"

    def test_invalid_typo_exit(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("EXI")

    def test_invalid_typo_place(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("PLAC")

    def test_invalid_typo_move(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("MOV")

    def test_invalid_typo_left(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("LEF")

    def test_invalid_typo_right(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("RIGH")

    def test_invalid_typo_report(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("REPOR")

    def test_invalid_exit_with_extra_param(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("EXIT ERROR")

    def test_invalid_move_with_extra_param(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("MOVE ERROR")

    def test_invalid_left_with_extra_param(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("LEFT ERROR")

    def test_invalid_right_with_extra_param(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("RIGHT ERROR")

    def test_invalid_error_with_extra_param(self):
        with pytest.raises(CommandError):
            command, _ = line_parser("REPORT ERROR")

    def test_invalid_place_coordinate_x_error(self):
        with pytest.raises(PlaceCommandError):
            command, coordinates = line_parser("PLACE string,1,NORTH")

    def test_invalid_place_coordinate_y_error(self):
        with pytest.raises(PlaceCommandError):
            command, coordinates = line_parser("PLACE 1,string,NORTH")

    def test_invalid_place_coordinate_direction_error(self):
        with pytest.raises(PlaceCommandError):
            command, coordinates = line_parser("PLACE 1,1,NORT")

