import pytest


@pytest.fixture
def board():
    """A simple fixture providing a robot instance"""
    from board import Board
    return Board()
