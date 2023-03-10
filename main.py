import pytest
import allure


def test_methodA():
    allureLogs("Launching app")
    allureLogs("This a Method A Step-1")
    allureLogs("This a Method A Step-2")
    print("This is method A")


def test_methodB():
    print("This is method B")
    allureLogs("This a Method B")


@pytest.mark.skip
def test_methodC():
    print("This is method C")


def test_methodD():
    print("This is method D")
    assert True


def allureLogs(text):
    with allure.step(text):
        pass






# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert "h" in x
#