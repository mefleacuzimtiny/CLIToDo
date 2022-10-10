

KEYWORDS = {
    "newvalue": "NEWVALUE",
    "add": "ADD",
    "remove": "REMOVE",
    "edit": "EDIT",
    "display": "DISPLAY",
    "prioritize": "PRIORITIZE",
    "move": "MOVE"
}

def tokenize(text, prefix):                                         # TODO: add an ILLEGAL token for unrecognized characters
    text += '\n'

    token_txt: str = ""
    t_len = 0
    kind: str = ""
    inquotes = False
    stored_tokens = {}
    
    if text[0] != prefix:
        raise ValueError(f"Invalid prefix! The defined prefix is {prefix}")

    for pos, char in enumerate(text, start = 1):
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

            case letter if char.isalpha() and inquotes == False:
                t_len+=1

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
            
            case illegal if not(illegal.isalpha() or illegal.isdigit() or illegal == ':' or illegal == '"' or illegal.isspace() or inquotes):
                t_len+=1
                if pos <= len(text):
                    kind = 'ILLEGAL'
                    token_txt = text[pos-t_len: pos]
                    t_len = 0

        if kind == "ILLEGAL":
            raise ValueError(f"Illegal token '{token_txt}'")
        if kind != None:
            stored_tokens[kind] = token_txt
    return stored_tokens


if __name__ == "__main__":
    while True:
        command = input('> ')
        try:
            print(tokenize(text = command, prefix = '/'))
        except ValueError as e:
            print(str(e))