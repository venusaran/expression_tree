import unittest
from main import infix_to_postfix, TreeBuilder


class TestEquations(unittest.TestCase):
    def test_results_1(self):
        expression = "4x(6x2)"
        postfix = infix_to_postfix(expression)
        obj = TreeBuilder()
        exp_tree = obj.build_tree(postfix)
        self.assertEqual(exp_tree.evaluate(), 48, "The results is wrong: TEST1")

    def test_results_2(self):
        expression = "2x(6÷2)"
        postfix = infix_to_postfix(expression)
        obj = TreeBuilder()
        exp_tree = obj.build_tree(postfix)
        self.assertEqual(exp_tree.evaluate(), 6, "The results is wrong: TEST2")

    def test_results_3(self):
        expression = "(9x4)-(6-2)+4"
        postfix = infix_to_postfix(expression)
        obj = TreeBuilder()
        exp_tree = obj.build_tree(postfix)
        self.assertEqual(exp_tree.evaluate(), 36, "The results is wrong: TEST3")

    def test_results_4(self):
        expression = "8x(6÷2)"
        postfix = infix_to_postfix(expression)
        obj = TreeBuilder()
        exp_tree = obj.build_tree(postfix)
        self.assertEqual(exp_tree.evaluate(), 24, "The results is wrong: TEST4")


if __name__ == '__main__':
    unittest.main()
