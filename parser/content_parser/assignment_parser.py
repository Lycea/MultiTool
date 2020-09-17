""" WORD ASSSIGNMENT ::= TABLE|WORD|NUMBER|STRING  NEW_LINE"""

from tokenizer.token import cTokenList
from content_parser.node import *

from content_parser.table_parser import *


class cAssignmentParser():
    def __init__(self):
        pass

    def match(self,token_list):
        token_list = cTokenList(tokens=token_list)
        if token_list.many_check(["WORD","ASSIGNMENT"])==True:
            print("we hava the start of an assignment")

            #ok now check if the following is a word and a new line
            #this would be a simple assignment in the mean of a int /double or similyr
            if token_list.many_check(["WORD"],start_idx=2) == True:
                #fround something,nice! retrn node + count
                print("found a word ...")
                base_count = 4
                new_lines = token_list.count_new_lines(start=base_count)
                return cNode("ASSIGNMENT", base_count+new_lines, tokens=[token_list.list[:base_count+new_lines]])


            #found some string
            elif token_list.many_check(["STRING_INDICATOR","WORD","STRING_INDICATOR"],start_idx=2) ==True:
                print("Found a string...")
                base_count =5
                new_lines=token_list.count_new_lines(start=base_count)

                return cNode("ASSIGNMENT",base_count+new_lines,tokens=[token_list.list[:base_count+new_lines]])

            # found some empty string
            elif token_list.many_check(["STRING_INDICATOR", "STRING_INDICATOR"], start_idx=2) == True:
                print("Found a empty string...")
                base_count = 4
                new_lines = token_list.count_new_lines(start=base_count)

                return cNode("ASSIGNMENT", base_count + new_lines, tokens=[token_list.list[:base_count + new_lines]])
            else:
                print("nothing of the above,try tables...")
                table_result=cTableParser().match(cTokenList(tokens=token_list.list[2:]))
                if table_result:
                    return cNode("ASSIGNMENT",2+table_result.consumed,childs=[table_result],tokens=token_list.list[:table_result.consumed+2])
                else:
                    return cNode.null()




        return None
