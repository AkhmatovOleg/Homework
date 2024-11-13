import main
import unittest


class MainTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(main.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(main.mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(main.div(6, 3), 2.0)


if __name__ == '__main__':
    unittest.main()


# def test_add():
#     if main.add(1, 2) == 3:
#         print("Test add is ok")
#     else:
#         print('test is not ok')
#
#
# def test_sub():
#     if main.sub(2, 1) == 1:
#         print("Test sub is ok")
#     else:
#         print('test is not ok')
#
#
# def test_mul():
#     if main.mul(2, 3) == 6:
#         print("Test mul is ok")
#     else:
#         print('test is not ok')
#
#
# def test_div():
#     if main.div(6, 3) == 2.0:
#         print("Test div is ok")
#     else:
#         print('test is not ok')
#
#
# test_add()
# test_sub()
# test_mul()
# test_div()
