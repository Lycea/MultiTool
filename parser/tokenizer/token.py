class cToken():
    def __init__(self,name="NULL",value="NULL"):
        self.name=name
        self.value=value

    @staticmethod
    def end_of_file():
        #print("end of file")
        return cToken("EOF","")
    @staticmethod
    def null():
        return False

    def getSize(self):
        return len(self.value)

    def getClean(self):
        return self.value.strip()

    def __str__(self):
        return self.name + "  "+self.value





class cTokenList():
    def __init__(self):
        self.__list=[]
        pass

    def add(self,token):
        self.__list.append(token)

    def print(self):
        for tok in self.__list:
            print(tok)

    def clean(self):
        pass




