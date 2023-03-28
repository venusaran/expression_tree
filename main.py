from abc import ABC, abstractmethod

'''
Method to convert infix equation to postfix notation
'''


def infix_to_postfix(expression):
    Operators = {'+', '-', 'x', '÷', '(', ')', '^'}      # supported operators
    Priority = {'+': 1, '-': 1, 'x': 2, '÷': 2, '^': 3}  # dictionary holding priorities of operators
    stack = []
    output = ''

    for character in expression:
        if character not in Operators:  # if an operand append in postfix expression
            output += character
        elif character == '(':  # else Operators push onto stack
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()
            stack.append(character)
    while stack:
        output += stack.pop()
    return output


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class MyNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def evaluate(self) -> int:
        x = self.val
        if x.isdigit():
            return int(x)

        left, right = self.left.evaluate(), self.right.evaluate()
        if x == '+':
            return left + right
        if x == '-':
            return left - right
        if x == 'x':
            return left * right
        if x == '÷':
            return left // right


"""    
This is the TreeBuilder class.
returns the expression tree representing it as a Node.
"""


class TreeBuilder(object):
    def build_tree(self, postfix: str) -> 'Node':
        stk = []
        for s in postfix:
            node = MyNode(s)
            if not s.isdigit():
                node.right = stk.pop()
                node.left = stk.pop()
            stk.append(node)
        return stk[-1]


"""
TreeBuilder object will be instantiated and called
"""
if __name__ == '__main__':
    session = True
    while session:
        try:
            expression = input('Enter your mathematical expression, Press Q to Exit> ')
            if expression == 'Q' or expression == 'q':
                break
            postfix = infix_to_postfix(expression)
            print(f'POSTFIX Notation:{postfix}')
            obj = TreeBuilder()
            exp_tree = obj.build_tree(postfix)
            answer = exp_tree.evaluate()
            print(answer)
        except ValueError:
            pass
