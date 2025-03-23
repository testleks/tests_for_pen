import pytest
from Pen import Pen


def test_default_ink(default_pen):
    assert default_pen.ink_container_value == 1000


def test_default_size_letter(default_pen):
    assert default_pen.size_letter == 1.0


def test_default_get_color(default_pen):
    assert default_pen.get_color() == "blue"


def test_custom_get_color(small_ink_pen):
    assert small_ink_pen.get_color() == "black"


def test_check_pen_state(default_pen, empty_pen):
    assert default_pen.check_pen_state() is True
    assert empty_pen.check_pen_state() is False


def test_do_something_else(capfd):
    pen = Pen(color="black")
    pen.do_something_else()
    captured = capfd.readouterr()
    assert "black" in captured.out


def test_write_long_text(default_pen):
    text = "Example" * 200
    written_text = default_pen.write(text)
    assert len(written_text) == 1000


def test_write_without_ink():
    pen = Pen(ink_container_value=0)
    assert pen.write("Example") == ""


def test_write_partial_word(small_ink_pen):
    result = small_ink_pen.write("Example")
    assert result == "Example"[:2]


def test_remain_ink(small_ink_pen):
    result = small_ink_pen.write("Example")
    assert small_ink_pen.ink_container_value == 1


def test_write_empty_string(default_pen):
    assert default_pen.write("") == ""


def test_empty_write(empty_pen):
    assert empty_pen.write("Test") == ""


def test_negative_ink(negative_ink_pen):
    assert negative_ink_pen.ink_container_value >= 0


def test_negative_size_letter(negative_size_letter_pen):
    assert negative_size_letter_pen.size_letter > 0
