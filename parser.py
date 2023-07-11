from typing import Optional, Callable

from mathematics import *


operators: dict = {
    "+": (1, 2, add),
    "-": (1, 2, sub),
    "~": (5, 1, unsub),
    "*": (2, 2, mul),
    "/": (2, 2, div),
    "^": (3, 2, power),
    "sqrt": (5, 1, sqrt),
    "root": (5, 2, root),
    "sin": (4, 1, sin),
    "cos": (4, 1, cos),
    "tan": (4, 1, tan),
    "ctg": (4, 1, ctg),
    "arcsin": (4, 1, arcsin),
    "arccos": (4, 1, arccos),
    "arctan": (4, 1, arctan),
    "arcctg": (4, 1, arcctg),
    "log": (5, 2, log),
    "ln": (5, 1, ln),
    "(": (10, 0, None),
    ")": (10, 0, None),
}


operands = "0123456789."


class Token:
    value: float | str | list
    is_operand: bool
    is_operator: bool
    priority: int

    def __repr__(self):
        return str(self.value)


class Operand(Token):
    is_operand: bool = True
    is_operator: bool = False

    def __init__(self, value: float):
        self.value = value


class Operator(Token):
    priority: int
    number_of_operands: int
    method: Optional[Callable]

    def __init__(self, value: str):
        self.value = value
        self.priority = operators[self.value][0]
        self.number_of_operands = operators[self.value][1]
        self.method = operators[self.value][2]
        self.is_operand = False
        self.is_operator = True


class Parser:
    raw_query: str
    list_query: list[Token]
    rpn_query: list[Token]
    output: float | int

    def __init__(self, raw_query: str | None = None):
        self.raw_query = raw_query

    def append_list(self, current: str):
        if not hasattr(self, "list_query"):
            self.list_query = []
        if current in operators.keys():
            self.list_query.append(Operator(current))
        else:
            if not current:
                pass
            else:
                try:
                    value = float(current)
                    self.list_query.append(Operand(value))
                except ValueError:
                    raise ValueError(
                        f"Unsupported operand or operator: |{current}|"
                    )

    def parse_to_in(self):
        current: str = ""
        previous_char = ""
        for char in self.raw_query:
            if char == " ":
                self.append_list(current)
                current = ""
                previous_char = char
                continue

            if char and char in operators:
                self.append_list(current)
                current = ""
                self.append_list(char)
                previous_char = char
                continue

            if (
                    char not in operands
                    and previous_char in operands
            ) or (
                    char in operands
                    and previous_char not in operands
            ):
                if " " not in (char, previous_char):
                    self.append_list(current)
                    current = ""

            if previous_char.isalpha():
                if not char.isalpha():
                    self.append_list(current)

            current += char
            previous_char = char
        else:
            self.append_list(current)

    def parse_to_rpn(self):
        op_stack: list = []
        rpn_list: list = []

        for token in self.list_query:
            if token.is_operand:
                rpn_list.append(token)
                continue
            if token.value == "(":
                op_stack.append(token)
                continue
            if token.value == ")":
                while True:
                    op = op_stack.pop()
                    if op.value == "(":
                        break
                    rpn_list.append(op)
                continue
            if token.is_operator:
                index = self.list_query.index(token)
                previous = self.list_query[index - 1] if index else None
                if token.value == "-" and (
                        previous is None or (
                        previous.is_operator
                        and previous.value != ")"
                    )
                ):
                    token.value = "~"
                    token.number_of_operands = 1
                    token.method = unsub
                while True:
                    if op_stack:
                        check_op = op_stack[-1]
                        if check_op.value == "(":
                            break
                        if check_op.priority >= token.priority:
                            op_to_rpn = op_stack.pop()
                            rpn_list.append(op_to_rpn)
                        else:
                            break
                    else:
                        break
                op_stack.append(token)
        else:
            while True:
                if op_stack:
                    rpn_list.append(op_stack.pop())
                else:
                    break
        self.rpn_query = rpn_list

    def evaluate(self):
        stack: list = []
        for token in self.rpn_query:
            if token.is_operand:
                stack.append(token)
                continue
            if token.is_operator:
                number = token.number_of_operands
                if number == 1:
                    operand = stack.pop()
                    result = token.method(operand.value)
                elif number == 2:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = token.method(operand1.value, operand2.value)
                else:
                    raise Exception("wtf")
                stack.append(Operand(result))
        self.output = stack.pop().value
