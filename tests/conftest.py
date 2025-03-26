import pytest
from Pen import Pen
import allure


with allure.step("Create default pen"):
    @pytest.fixture
    def default_pen():
        return Pen()


@pytest.fixture
def small_ink_pen():
    return Pen(ink_container_value=5, size_letter=2, color="black")


with allure.step("Create default pen"):
    @pytest.fixture
    def empty_pen():
        return Pen(ink_container_value=0)


@pytest.fixture
def negative_ink_pen():
    return Pen(ink_container_value=-5)


@pytest.fixture
def negative_size_letter_pen():
    return Pen(size_letter=-5)
