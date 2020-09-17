from content_parser.node import cNode
from content_parser.assignment_parser import cAssignmentParser
from content_parser.helpers import *


class cContextParser:
    def __init__(self):
        self.__node_list = []
        pass


    def parse(self,token_list):
        results=match_star(token_list,cAssignmentParser())

        return results
