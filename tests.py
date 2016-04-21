#!/usr/bin/env python3
import unittest
import lib


class TestSleepIn(unittest.TestCase):
    def test1(self):
        self.assertTrue(lib.sleep_in(False, False))

    def test2(self):
        self.assertFalse(lib.sleep_in(True, False))

    def test3(self):
        self.assertTrue(lib.sleep_in(False, True))

    def test4(self):
        self.assertTrue(lib.sleep_in(True, True))


class TestMonkeyTrouble(unittest.TestCase):
    def test1(self):
        self.assertTrue(lib.monkey_trouble(True, True))

    def test2(self):
        self.assertTrue(lib.monkey_trouble(False, False))

    def test3(self):
        self.assertFalse(lib.monkey_trouble(True, False))

    def test4(self):
        self.assertFalse(lib.monkey_trouble(False, True))


class TestSumDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.sum_double(1, 2), 3)

    def test2(self):
        self.assertEqual(lib.sum_double(3, 2), 5)

    def test3(self):
        self.assertEqual(lib.sum_double(2, 2), 8)

    def test4(self):
        self.assertEqual(lib.sum_double(-1, 0), -1)

    def test5(self):
        self.assertEqual(lib.sum_double(3, 3), 12)

    def test6(self):
        self.assertEqual(lib.sum_double(0, 0), 0)

    def test7(self):
        self.assertEqual(lib.sum_double(0, 1), 1)

    def test8(self):
        self.assertEqual(lib.sum_double(3, 4), 7)


class TestDiff21(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.diff21(19), 2)

    def test2(self):
        self.assertEqual(lib.diff21(10), 11)

    def test3(self):
        self.assertEqual(lib.diff21(21), 0)

    def test4(self):
        self.assertEqual(lib.diff21(22), 2)

    def test5(self):
        self.assertEqual(lib.diff21(25), 8)

    def test6(self):
        self.assertEqual(lib.diff21(30), 18)

    def test7(self):
        self.assertEqual(lib.diff21(0), 21)

    def test8(self):
        self.assertEqual(lib.diff21(1), 20)

    def test9(self):
        self.assertEqual(lib.diff21(2), 19)

    def test10(self):
        self.assertEqual(lib.diff21(-1), 22)

    def test11(self):
        self.assertEqual(lib.diff21(-2), 23)

    def test12(self):
        self.assertEqual(lib.diff21(50), 58)


class CountEvens(unittest.TestCase):
    def test1(self):
        self.assertEqual(lib.count_evens([2, 1, 2, 3, 4]), 3)

    def test2(self):
        self.assertEqual(lib.count_evens([2, 2, 0]), 3)

    def test3(self):
        self.assertEqual(lib.count_evens([1, 3, 5]), 0)

    def test4(self):
        self.assertEqual(lib.count_evens([]), 0)

    def test5(self):
        self.assertEqual(lib.count_evens([11, 9, 0, 1]), 1)

    def test6(self):
        self.assertEqual(lib.count_evens([2, 11, 9, 0]), 2)

    def test7(self):
        self.assertEqual(lib.count_evens([2]), 1)

    def test8(self):
        self.assertEqual(lib.count_evens([2, 5, 12]), 2)


class TestXYZThere(unittest.TestCase):
    """
    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True
    xyz_there('abcxy') → False
    xyz_there('xyz') → True
    xyz_there('xy') → False
    xyz_there('x') → False
    xyz_there('') → False
    xyz_there('abc.xyzxyz') → True
    xyz_there('abc.xxyz') → True
    xyz_there('.xyz') → False
    xyz_there('12.xyz') → False
    xyz_there('12xyz') → True
    xyz_there('1.xyz.xyz2.xyz') → False
    """
    def test1(self):
        self.assertTrue(lib.xyz_there('abcxyz'))

    def test2(self):
        self.assertFalse(lib.xyz_there('abc.xyz'))

    def test3(self):
        self.assertTrue(lib.xyz_there('xyz.abc'))

    def test4(self):
        self.assertFalse(lib.xyz_there('abcxy'))

    def test5(self):
        self.assertTrue(lib.xyz_there('xyz'))

    def test6(self):
        self.assertFalse(lib.xyz_there('xy'))

    def test7(self):
        self.assertFalse(lib.xyz_there('x'))

    def test8(self):
        self.assertFalse(lib.xyz_there(''))

    def test9(self):
        self.assertTrue(lib.xyz_there('abc.xyzxyz'))

    def test10(self):
        self.assertTrue(lib.xyz_there('abc.xxyz'))

    def test11(self):
        self.assertFalse(lib.xyz_there('.xyz'))

    def test12(self):
        self.assertFalse(lib.xyz_there('12.xyz'))

    def test13(self):
        self.assertTrue(lib.xyz_there('12xyz'))

    def test14(self):
        self.assertFalse(lib.xyz_there('1.xyz.xyz2.xyz'))


class TestIsPrime(unittest.TestCase):
    def test1(self):
        self.assertTrue(lib.is_prime(2))

    def test2(self):
        self.assertTrue(lib.is_prime(3))

    def test3(self):
        self.assertTrue(lib.is_prime(5))

    def test4(self):
        self.assertTrue(lib.is_prime(7))

    def test5(self):
        self.assertTrue(lib.is_prime(11))

    def test6(self):
        self.assertTrue(lib.is_prime(13))

    def test7(self):
        self.assertTrue(lib.is_prime(17))

    def test8(self):
        self.assertTrue(lib.is_prime(19))

    def test9(self):
        self.assertTrue(lib.is_prime(23))

    def test10(self):
        self.assertFalse(lib.is_prime(4))

    def test11(self):
        self.assertFalse(lib.is_prime(6))

    def test12(self):
        self.assertFalse(lib.is_prime(8))

    def test13(self):
        self.assertFalse(lib.is_prime(9))

    def test14(self):
        self.assertFalse(lib.is_prime(10))

    def test15(self):
        self.assertFalse(lib.is_prime(100))

if __name__ == '__main__':
    unittest.main()
