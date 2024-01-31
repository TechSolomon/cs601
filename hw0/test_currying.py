from currying import f, curry2, curryN

import unittest


class TestCurrying(unittest.TestCase):
    def test_f(self):
        self.assertEqual(f(20, 30), 50)

    def test_curry2(self):
        self.assertNotEqual(curry2(f)(10), f(10))
        self.assertEqual(curry2(f)(20)(30), f(20, 30))

    def test_curryN(self):
        self.assertNotEqual(curryN(f, -1337), f)
        self.assertEqual(curryN(f, 0), f)
        self.assertEqual(curryN(f, 1)(20), f(20))
        self.assertEqual(curryN(f, 2)(40)(60), f(40, 60))
        self.assertEqual(curryN(f, 3)(80)(100)(120), f(80, 100, 120))


if __name__ == "__main__":
    unittest.main()
