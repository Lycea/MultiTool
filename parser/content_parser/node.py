class cNode():
    def __init__(self,name,size,childs=[],tokens=[]):
        self.name =name
        self.childs=childs
        self.consumed = size
        self.used_tokens = tokens

    def add_child(self,node):
        self.childs.append(node)
        self.consumed+= node.consumed


    @staticmethod
    def null():
        return False