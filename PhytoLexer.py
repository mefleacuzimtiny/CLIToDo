from dataclasses import dataclass
from enum import Enum, auto

# /add "task task task" 5 Incompleted
# /remove 5 Completed
# /remove 3 Priorities
# /prioritize 5 1
# /edit 4 newvalue:"text"/5 Incompleted
# /move 4 Incompleted 3 Completed

class TokenKind(Enum):
    ILLEGAL = auto()
    END_OF_LINE = auto()                                #All the types the tokens could represent listed here.
    PREFIX = auto()                                     #Prefis is separate so we can have the feature to change it at will
    ADD = auto()                                        #Illegal token implies that the token is not allowed.
    REMOVE = auto()                                     #End of Line is to specify the end of the command.
    PRIORITIZE = auto()                                 #Number will be further classified into LHSPosition and RHSPosition in the parser
    EDIT = auto()                                       #Newvalue and colon is separate for hybric-static typing type stuff with other parts of the command.
    MOVE = auto()                                       #Text selects any substring.
    NUMBER = auto()                                     #Bareword selects any word without quotes.
    NEWVALUE = auto()
    COLON = auto()
    SUBSTRING = auto()
    BAREWORD = auto()

@dataclass
class Token:
    kind: TokenKind
    text: str

KEYWORDS = {
    "add": TokenKind.ADD,
    "remove": TokenKind.REMOVE,
    "prioritize": TokenKind.PRIORITIZE,
    "edit": TokenKind.EDIT,
    "move": TokenKind.MOVE,
    "newvalue": TokenKind.NEWVALUE,
}


# The lexer will iterate through the string, and use the above classes to label the input text (which is self.text)
class Lexer:
    def __init__(self, text, prefix):
        self.text = text
        self.prefix = prefix
        self.position = 0
        self.token_start = 0
    
    def lexToken(self) -> Token: #means that lex() returns a Token object
        while self.position < len(self.text) and self.text[self.position].isspace():
            self.position += 1                  #set the starting position at 1

        self.token_start = self.position
        kind = TokenKind.ILLEGAL
        token_text :str = ""

        if self.position == len(self.text):
            kind = TokenKind.END_OF_LINE

        else:
            match self.text[self.position]:                     #if the current character in the text is any of these cases, then handle them according to the case
                case self.prefix:                                       #if it's the prefix "/" or anything, move right, and store the PREFIX token
                    self.position += 1
                    kind = TokenKind.PREFIX
                
                case ":":                                               #if it's a colon, move right, and store the COLON token
                    self.position += 1
                    kind = TokenKind.COLON
                
                case letter if letter.isalpha():                        #if it's a letter, which it is if the character is an alphabet, then
                    while (self.position < len(self.text) and           # move right until you hit the end of the line,
                    self.text[self.position].isalpha()):                        # or no more alphabets are found...
                        self.position += 1                                                          
                    else:                                                                           
                        token_text = self.text[self.token_start : self.position]        #Store the selected text in the token

                        try:                                                                        # ...then try to store one of the KEYWORD tokens,
                            kind = KEYWORDS[token_text]                                             # which you can't if the keyword isn't defined in the KEYWORDS dict,
                        except KeyError:                                                            # and except that error to check
                            if token_text[0].isupper():                                             # if the first letter is uppercase,
                                kind = TokenKind.BAREWORD                                           # in which chase, store a BAREWORD token
                            else:
                                raise ValueError(f"{token_text} is not a valid keyword")
                
                case digit if digit.isdigit():                          #if it's a digit, which it is if the character is a number, then
                    while (self.position < len(self.text) and           # move right until you hit the end of the line,
                    self.text[self.position].isdigit()):                        # or no more digits are found...
                        self.position += 1
                    
                    else:
                        token_text = self.text[self.token_start : self.position]        #Store the selected text in the token
                        kind = TokenKind.NUMBER                                                     # in which case, store a NUMBER token
                    
                case '"':                                               #if it's a starting quote, move right to select text excluding the quotes, then
                    self.position += 1
                    while (self.text[self.position] != '"' and              # move right until you hit the ending quote,
                    self.position < len(self.text)):                        # or you hit the end of the line...
                        self.position += 1

                    else:                                                   
                        self.position += 1                                  # ...then move right
                        if self.position == len(self.text) and self.text[self.position - 1] != '"': # and if the end of the line is reached
                            raise ValueError("Unterminated String")                                 # and there was no ending quote, then raise an error

                        kind = TokenKind.SUBSTRING                          # otherwise, store a SUBSTRING token
        if kind == TokenKind.ILLEGAL:
            raise ValueError(f"what even is '{self.text[self.position]}'???")

        if token_text == "":                                                            #if there is no text inputted,
            token_text = self.text[self.token_start : self.position]                        # then token_text will have a blank string

        return Token(kind, token_text)          #push out the token with it's type and the text it's associated with.


if __name__=="__main__":
    text = '/add 5'
    lexer = Lexer(text, "/")
    while True:
        token = lexer.lexToken()
        if token.kind == TokenKind.END_OF_LINE:
            break
        print(token.kind, f'"{token.text}" at {lexer.position}')
# The Hull is animalistic instinct. It it the nature of being.
# Lexer labels, Parser organizes.
# /edit 4 newvalue:"changed value 50" Incompleted