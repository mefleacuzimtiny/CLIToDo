# TODO: build a parser
from FleaLexer import tokenize, op_keywords

tokens = tokenize(text = '/edit 4 to:"5fdsafdafda fdsafdas"', prefix = '/')
print(tokens)





"""
TODO:
RULES:
    each function has it's own order of tokens
    1. /edit [number] [newvalue][colon][number] or [substring]
    2. /add [substring] [number] [bareword]
    3. /remove [number] [bareword]
    4. /display [bareword] or [all]
    5. /prioritize [number] [number]
    6. /move [number] [bareword] [number] [bareword]
    7. /save [bareword] or [all]
    8. /exit
    9. /help
"""

for token, txt in tokens:
    print(token, txt)

def checkOrder(tokenlist) -> bool:
    comparison = 
    if tokenlist[1] not in op_keywords:
        return False


def parse(tokenlist):
    """
    TODO:
    The parser will first check if the tokens are in the right order for each rule
    Then, it will generate a list of the text of the values
    Then, every value in this list will be converted to it's appropriate datatype depending on what kind of token it is,
    Then, the list will be passed on as a tuple to unpack in the util file into the approprate funtion. 
    """
    match tokenlist[1]:
        case "edit":
            pass
        case "edit":
            pass
        case "edit":
            pass
        case "edit":
            pass
        case "edit":
            pass
        case "edit":
            pass
        case "edit":
            pass
    pass