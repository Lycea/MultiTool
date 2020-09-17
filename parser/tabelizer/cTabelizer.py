


class cTabelizer:
    def __init__(self):
        self.return_dict ={}
        self.__parse_level=1

    def __get_word(self,tok_list):
        words =[]
        for token in tok_list:
            if token.name == "WORD":
                words.append(token.value)
        return words


    def __recurr_tree(self,tree,par=None):
        self.__parse_level+=1
        print("  "*self.__parse_level+tree.name)
        if len(tree.childs) >0:
            if tree.name == "ASSIGNMENT":
                print("  "*self.__parse_level,self.__get_word(tree.used_tokens))

            for child in tree.childs:
                self.__recurr_tree(child)
        else:
            if tree.name == "TABLE_ROW":
                for token in tree.used_tokens:
                    print("  "*self.__parse_level,token)
            elif tree.name == "ASSIGNMENT":
                print(self.__get_word(tree.used_tokens[0]))
                print("  "*self.__parse_level,tree.used_tokens[0][0],tree.used_tokens[0][2])
                #for token in tree.used_tokens[0]:
                #    print("  "*self.__parse_level,token)


        self.__parse_level-=1
        pass


    def parse(self,tree):
        print("hi")
        print(tree)
        self.__recurr_tree(tree)


