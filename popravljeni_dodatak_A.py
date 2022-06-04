import getpass
import unittest

import bcrypt

passwd = b'123'
hashed = bcrypt.hashpw(passwd, bcrypt.gensalt(10))


class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b

    def pick_one_digit_number(self) -> int:
        """Returns one_digit_number. If a>10 returns NaN."""
        return [range(10)][self.a]


class TestA(unittest.TestCase):

    def testAssertZeroDivision(self, msg=None):

        operation_manager = OperationsManager(a=3, b=1)

        try:
            if (operation_manager.b == 0):
                if (operation_manager.perform_division() is not math.nan):
                    self.fail(self._formatMessage(msg, "Division result is not NaN"))

        except ZeroDivisionError:
            self.fail(self._formatMessage(msg, "Division result is not NaN"))

    def testAssertListOutOfRange(self, msg=None):

        operation_manager = OperationsManager(a=3, b=12)

        try:
            if (operation_manager.a >= 10):
                if (operation_manager.pick_one_digit_number() is not math.nan):
                    self.fail(self._formatMessage(msg, "Chosen number is not NaN"))

        except IndexError:
            self.fail(self._formatMessage(msg, "Chosen number is not NaN"))


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    if user != "root" or not bcrypt.checkpw(passwd, hashed):
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())
    unittest.main()
