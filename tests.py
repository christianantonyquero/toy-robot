"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""


class TestClass:
    """
    A class that represent the testing for this solution
    """
    def test_A(self):
        expected_output = "0,1,NORTH"
        # PLACE
        # 0, 0, NORTH
        # MOVE
        # REPORT

    def test_B(self):
        expected_output = "0,0,WEST"
        # PLACE
        # 0, 0, NORTH
        # LEFT
        # REPORT

    def test_C(self):
        expected_output = "3,3,NORTH"
        # PLACE
        # 1, 2, EAST
        # MOVE
        # MOVE
        # LEFT
        # MOVE
        # REPORT
