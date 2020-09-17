from tokenizer.token import *

from tokenizer.base_token import cBaseToken
from tokenizer.word_token import cWordToken

class cTokenizer():
    def __init__(self):
        print("hi")
        self.tokens = cTokenList()


        pass
    def __get_single_token(self):
        scanners = [cBaseToken(),cWordToken()]

        for scanner in scanners:
            token = scanner.fromString(self.to_prozess_text)
            if not token:
                continue
            else:
                return token



    def __run_whole_text(self):

        while self.to_prozess_text.strip() != "" and self.to_prozess_text.strip() != None:
            print("----------------------------------------------------------------")
            print(self.to_prozess_text)

            token =self.__get_single_token()

            self.tokens.add(token)
            self.to_prozess_text=self.to_prozess_text[token.getSize():]


        self.tokens.add(cToken.end_of_file())


    def tokenize(self,txt):

        self.to_prozess_text = txt
        self.__run_whole_text()
        self.tokens.clean()
        self.tokens.print()


        return self.tokens
