from numbers import Number

from fastmcp import FastMCP

from calculator.evaluator import Evaluator


mcp = FastMCP(name = 'calculator')


@mcp.tool
async def evaluate(expression: str) -> Number:
    """Evaluate basic mathematical expression written in Python syntax"""
    # TODO: send error message properly
    return Evaluator.eval(expression)


if __name__ == '__main__':
    mcp.run()

