from parser import Parser

if __name__ == "__main__":
    while True:
        raw_query = input()
        try:
            parser = Parser(raw_query)
            parser.parse_to_in()
            parser.parse_to_rpn()
            parser.evaluate()
            print(parser.output)
        except Exception as ex:
            print(f"Error: {ex}")
