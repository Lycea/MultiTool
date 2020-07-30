from tokenizer.token import cToken
from tokenizer.base_token import cBaseToken

class cWordToken(cBaseToken):
    def __init__(self):
        pass

    def fromString(self,txt):
        #ok now iterate the string till there is a token
        token_text = ""

        for char in txt:
            token_return= cBaseToken().fromString(char)

            #if we got a token then just go back and let it do its thing
            if token_return !=False and token_return!= None:
                break
            else:
                token_text+=char

        if token_text!= "":

            return cToken("WORD",token_text)
        else:
            return False