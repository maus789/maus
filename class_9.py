import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", fornata = "We have next logging wessage:%(asctime)s:%(levelnane)s %(message)s")
logging.debug("debug")
logging.info("info")


import logging
logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have next logging message:%(asctine)s:%(levelname)s -%(message)s")
try:
    print(10/8)
except Exception:
    logging.exception("Exception")


if 2+2 == 4:
print("In fact, 2+ 2 equals 4")


assert 2+2== 5, "wrong assert"


'''
>>> 2+2
5
'''
if __name__ == "__lesson_8a__":
 import doctest
 doctest.testmod()


import unittest
from lesson_8a import
class My_Test(unittest.TestCase):
    def test_args_(self):
        self.assertEqual(adder(2, 2), 4)
    def test_kwargs (self):
        self.assertEqual(adder(  a = 10, b = 11), 21)
    def test_mixed (self):
        self.assertEqual(adder( 1, a = 2), 3)

    def test diff (self):
        x = 10
        y = 0
        self.assertEqual(adder( 0, -5, y, a = x), 5)
    def test_wrong_datatype (self):
        self.assertEqual(adder( "5", "abc", 10), 15)
if __name__ =="_lesson_8a__":
 unittest.main()