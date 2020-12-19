from aocd import get_data, submit
import pyparsing

def parse_expression(expr):
    """Recursive expression parsing. The expressions must be present in a structured format."""
    child_expressions = []
    for child_expr in expr:
        if isinstance(child_expr, pyparsing.ParseResults):
            child_expressions.append(parse_expression(child_expr))
        else:
            child_expressions.append(child_expr)
    while len(child_expressions) > 2:
        res = eval("".join(map(str, child_expressions[0:3])))
        child_expressions = [res] + child_expressions[3:]
    return int(child_expressions[0])

if __name__ == "__main__":
    # Get problem input
    lines = get_data(day=18, year=2020).splitlines()

    # Set up the grammar and expression rules (Part A)
    calc_a = pyparsing.infixNotation(pyparsing.Word(pyparsing.nums), 
        [(pyparsing.oneOf("* +"), 2, pyparsing.opAssoc.LEFT)])
    expressions_a = [calc_a.parseString(line) for line in lines]

    # Solve Part A
    submit(sum(parse_expression(expr) for expr in expressions_a), part="a", day=18, year=2020)

    # Set up the grammar and expression rules (Part B)
    calc_b = pyparsing.infixNotation(pyparsing.Word(pyparsing.nums), 
        [(pyparsing.oneOf("+"), 2, pyparsing.opAssoc.LEFT), (pyparsing.oneOf("*"), 2, pyparsing.opAssoc.LEFT)])
    expressions_b = [calc_b.parseString(line) for line in lines]

    # Solve Part B
    submit(sum(parse_expression(expr) for expr in expressions_b), part="b", day=18, year=2020)
