text = '/add 5'
prefix = '/'


token_txt: str = ""
t_len = 0
kind: str = ""
inquotes = False

KEYWORDS = {
    "add": "ADD" 
}
for pos, char in enumerate(text):
    match char:
        case prefix if pos == 0 and inquotes == False:
            kind = "PREFIX"

        case ':':
            if inquotes == False:
                kind = "COLON"

        case letter if letter.isalpha() and inquotes == False:
            t_len+=1

            if not letter:                                                  #ERROR HERE!!!
                token_txt = text[pos-t_len : pos]
                
                try:
                    kind = KEYWORDS[token_txt]
                except KeyError:
                    if token_txt[0].isupper():
                        kind = "BAREWORD"
                    else:
                        raise ValueError(f"Invalid Keyword {token_txt}")
        
        case '"':
            inquotes = not inquotes
            t_len+=1
            if pos <= len(text) and inquotes == False:
                kind = "SUBSTRING"
                t_len = 0
            if pos > len(text):
                raise ValueError("Unterminated String")
 
        case digit if digit.isdigit() and inquotes == False:
            t_len+=1
            if pos <= len(text):
                kind = "NUMBER"
                token_txt = text[pos-t_len: pos]

    print(kind)
        