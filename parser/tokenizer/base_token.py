from tokenizer.token import *

class cBaseToken():
    def __init__(self):
        self.specials={
            "=": "ASSIGNMENT",
            "-": "MINUS",
            "{": "TABLE_START",
            "}":"TABLE_END",
            ",":"SEPERATOR",
            '"':"STRING_INDICATOR",

            "\n":"NEW_LINE"
        }


    def fromString(self,txt):
        if txt[0] in self.specials.keys():
            return cToken(self.specials[txt[0]],txt[0])
        else:
            return cToken.null()
