import ast
import operator as op
from numbers import Number


# Adapted from https://stackoverflow.com/a/9558001/1818110
class Evaluator:

    # List supported operators
    # and map from AST node to function implementation.
    operators = {
        ast.Add: op.add,
        ast.Sub: op.sub,
        ast.Mult: op.mul,
        ast.Div: op.truediv,
        ast.Pow: op.pow,
        ast.BitXor: op.xor,
        ast.USub: op.neg,
    }

    @staticmethod
    def eval(expression: str) -> Number:
        return Evaluator.eval_node(ast.parse(expression, mode = 'eval').body)

    @staticmethod
    def eval_node(node):
        match node:
            case ast.Constant(value) if isinstance(value, Number):
                return value
            case ast.BinOp(left, op, right):
                return Evaluator.operators[type(op)](
                    Evaluator.eval_node(left),
                    Evaluator.eval_node(right),
                )
            case ast.UnaryOp(op, operand):
                return Evaluator.operators[type(op)](
                    Evaluator.eval_node(operand),
                )
            case _:
                # TODO: will this report error properly?
                raise ValueError(node)

