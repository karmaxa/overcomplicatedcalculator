# overcomplicatedcalculator
It's just me trying to entertain myself decided to code a class-based calculator with Python


You can use it by simply launching main.py.
Input your string with math expression and calculator will calculate it.

Possible operators:
"""
- (
- )
- - | regular subtraction
- ~ | unary subtraction
- + | addition
- * | multiplication
- / | division
- ^ | exponentiation
- sqrt | square root. usage: sqrt(4)
- root | usage: root3(8) will give you 3rd root of 8 (e. g. 2)
- trigonometric functions | usage: func(num)
  + cos, sin, tan, ctg | provide values in radians
  + arcsin, arccos, arctan, arcctg
- log | logarithm. usage: log2(8) will give you log of 8 by base 2 (e.g. 3)
- ln | natural logarithm. usage: ln(10)
"""


Also parser.Parser can be used for parsing algebraic expression into inline notation (parser.Parser.parse_to_in()) or into polish notation (parser.Parser.parse_to_rpn()).
Usage of the parser:
"""
- initiate your query string
  > query = "2+2*2"
- create a new Parser object and provide a string to it
  > parser = Parser(query)
  > parser.raw_query
  < 2+2*2
- parse a query to inline list
  > parser.parse_to_in()
  > parser.list_query
  < [2.0, +, 2.0, *, 2.0]
- parse an inline list to a polish notation list
  > parser.parse_to_rpn()
  > parser.rpn_query
  < [2.0, 2.0, 2.0, *, +]
- evaluate the rpn expression
  > parser.evaluate()
  > parser.output
  < 6.0
"""

Note that none of Parser methods return anything. Parser saves every stage in itself and values at every stage are available at any time after they are generated.
