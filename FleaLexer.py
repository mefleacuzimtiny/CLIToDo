text = '/add 5 newvalue:"ass ass ass" sub'
text += '\n'
prefix = '/'


token_txt: str = ""
t_len = 0
kind: str = ""
inquotes = False

KEYWORDS = {
    "newvalue": "NEWVALUE",
    "add": "ADD",
    "sub": "SUBTRACT"
}

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

        case letter if letter.isalpha() and inquotes == False:
            t_len+=1

            if pos < len(text) and not text[pos].isalpha():                                                  #ERROR HERE!!!
                token_txt = text[pos-t_len : pos]

                if token_txt in KEYWORDS:
                    kind = KEYWORDS[token_txt]

                if token_txt[0].isupper():
                    kind = "BAREWORD"
                        
                if not (token_txt in KEYWORDS or token_txt[0].isupper()):
                    raise ValueError(f"Invalid Keyword {token_txt}")

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
            
        case digit if digit.isdigit() and inquotes == False:
            t_len+=1
            if pos <= len(text):
                kind = "NUMBER"
                token_txt = text[pos-t_len: pos]
                t_len = 0

    if kind != None: print(kind, token_txt)
    kind = None
        