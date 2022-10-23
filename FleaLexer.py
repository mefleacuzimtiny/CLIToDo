"""
TODO: take "inquotes = False" common
"""


op_keywords = {
    "add": "[NUMBER][SUBSTRING]",
    "remove": "[NUMBER][BAREWORD]",
    "prioritize": "[NUMBER][NUMBER]",
    "edit": "[NUMBER][NEWVALUE][COLON][NUMBER][COMMA][SUBSTRING]",
    "move": "[NUMBER][BAREWORD][NUMBER][BAREWORD]",
    "display": "[BAREWORD]/[ALL]",
    "save": "[BAREWORD]/[ALL]",
    "exit": None,
    "help": None
}

KEYWORDS = {
    "to": "NEWVALUE",
    "all": "ALL"
}

for word, args in op_keywords.items():
    KEYWORDS[word] = word.upper()

def tokenize(text, prefix):
    text += '\n'

    token_txt: str = ""
    t_len: int = 0
    kind: str = ""
    inquotes: bool = False
    stored_tokens: list = []
    
    if text[0] != prefix:
        raise ValueError(f"Invalid prefix! The defined prefix is {prefix}")

    for pos, char in enumerate(text, start = 1):
        kind = "ILLEGAL"
        match char:
            case prefix if pos == 1 and inquotes == False:
                t_len += 1
                kind = "PREFIX"
                token_txt = text[pos - t_len: pos]
                t_len = 0

            case colon if char == ':' and inquotes == False:
                t_len+=1
                kind = "COLON"
                token_txt = text[pos-t_len : pos]
                t_len = 0

            case comma if char == ',' and inquotes == False:
                t_len+=1
                kind = "COMMA"
                token_txt = text[pos-t_len : pos]
                t_len = 0

            case letter if char.isalpha() and inquotes == False:
                t_len+=1
                kind = None
                if pos < len(text) and not text[pos].isalpha():
                    token_txt = text[pos-t_len : pos]

                    if token_txt in KEYWORDS:
                        kind = KEYWORDS[token_txt]

                    if token_txt[0].isupper():
                        kind = "BAREWORD"

                    if not (token_txt in KEYWORDS or token_txt[0].isupper()):
                        raise ValueError(f"Invalid Keyword: {token_txt}")

                    t_len = 0

            case '"':
                inquotes = not inquotes
                
            case substring if inquotes == True:
                t_len+=1
                kind = None
                if pos < len(text) and text[pos] == '"':
                    kind = "SUBSTRING"
                    token_txt = text[pos - t_len: pos]
                    t_len = 0

                if pos == len(text):
                    raise ValueError("Unterminated String")
                
            case digit if char.isdigit() and inquotes == False:
                t_len+=1
                if pos <= len(text):
                    kind = "NUMBER"
                    token_txt = text[pos-t_len: pos]
                    t_len = 0

        if not char.isspace() and kind == "ILLEGAL" and char != '"' and char != ",":
            t_len+=1
            token_txt = text[pos-t_len: pos]
            t_len = 0
            raise ValueError(f"Illegal token '{token_txt}'")

        if kind != None and kind != "ILLEGAL":
            stored_tokens.append([kind, token_txt])
            kind = None

    return tuple(stored_tokens)


if __name__ == "__main__":
    while True:
        command = input('> ')
        try:
            print(tokenize(text = command, prefix = '/'))
        except ValueError as e:
            print(str(e))