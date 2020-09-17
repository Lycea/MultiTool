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
    def __init__(self,tokens=[]):
        self.list=tokens

        self.FIT = True
        self.NO_FIT = False
        pass

    def add(self,token):
        self.list.append(token)

    def print(self):
        for tok in self.list:
            print(tok)

    def clean(self):
        idx=len(self.list)-1
        while idx!= -1:
            token_ = self.list[idx]
            if token_.value.strip() == "" and token_.name!="NEW_LINE" and token_.name!="EOF":
                print("deleting since empty,and we dont care about empty stuff so space...")
                print(token_.name,token_.value,token_.getSize())
                self.list.remove(token_)
            idx-=1
        print("done cleanup...")

    def idx_is_type(self,idx,type):
        return self.list[idx].name == type

    def first_is_type(self,type):
        return self.list[0].name ==type


    def many_check(self,type_list,start_idx=0):

        for type in type_list:
            if self.idx_is_type(start_idx,type)==self.NO_FIT:
                return self.NO_FIT
            start_idx+=1

        #iterated all and did not break so success...
        return self.FIT

    def many_or_check(self,many_type_list_check):
        pass

    def count_repeat_of(self,repeat_type,start=0):
        new_line_count = 0
        while True:
            if self.list[start].name != repeat_type:
                break

            new_line_count+=1
            start+=1

        return new_line_count

    def count_new_lines(self,start=0):
       return self.count_repeat_of("NEW_LINE",start)





