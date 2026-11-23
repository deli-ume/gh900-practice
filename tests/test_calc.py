import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import calc  # noqa: E402


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)

    # 演習2：ここに subtract のテストを追加する
    # def test_subtract(self):
    #     self.assertEqual(calc.subtract(10, 3), 7)


if __name__ == "__main__":
    unittest.main()
