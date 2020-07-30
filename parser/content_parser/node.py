class cNode():
    def __init__(self,name,childs,size):
        self.name =name
        self.childs=[]
        self.size = size

    def add_child(self,node):
        self.childs.append(node)