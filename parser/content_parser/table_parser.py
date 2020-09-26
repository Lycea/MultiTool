from tokenizer.token import cTokenList
from content_parser.node import *
from content_parser.helpers import *

import sys
for module in sys.modules:
    print(module)

import content_parser.assign_parser 




"""TABLE-ROW:
    TABLE|ASSIGNMENT
"""
class cTableContent():
    def match(self,token_list):
        print(token_list)


        print("start matching row")
        result = match_first(token_list,[content_parser.assign_parser.cAssignmentParser(),cTableParser()])
        #if we get a result check if there is a
        if result:

            if type(token_list) == list:
                token_list = cTokenList(tokens=token_list)
            #check if we got a "," or some new lines
            sep_count=token_list.count_repeat_of("SEPERATOR",start=result.consumed)
            new_line_count=token_list.count_new_lines(start=result.consumed+sep_count)
            row_node = cNode("TABLE_ROW",result.consumed+sep_count+new_line_count,childs=[result])
            return row_node
        #check if we only got a simple word without asignment,this could be a simple {12,13} table
        else:
            if type(token_list) == list:
                token_list = cTokenList(tokens=token_list)
            #ok we got only a simple word...
            if token_list.first_is_type("WORD") :
                first_new_count = token_list.count_new_lines(start=1 )
                sep_count = token_list.count_repeat_of("SEPERATOR", start=1+first_new_count)
                new_line_count = token_list.count_new_lines(start=1 + sep_count+first_new_count)
                row_node = cNode("TABLE_ROW", 1 + sep_count + new_line_count+first_new_count,tokens=token_list.list[:1 + sep_count + new_line_count+first_new_count])
                return row_node

        return cNode.null()


"""TABLE
  TABLE_OPEN ::= TABLE_ROW(,) ::TABLE_CLOSE """


class cTableParser():
    def match(self,token_list):
        if type(token_list) == list:
            token_list = cTokenList(tokens=token_list)

        print("try matching table")

        if token_list.first_is_type("TABLE_START"):
            print("we got a table!!!!")

            print("cleaning out new lines...")
            print("check how long we can find new lines,that is ")
            new_lines = token_list.count_new_lines(start=1)
            print("Found new lines:",new_lines)

            print("now parse for rows...")
            results =match_star(cTokenList(tokens=token_list.list[1+new_lines:]),cTableContent())

            #ok now we got back some table rows
            if results :
                print("found rows:",len(results[0]))
                print("used tokens:",results[1])
                if len(results[0])== 0:
                    print("found no rows")

                if token_list.idx_is_type(results[1]+new_lines+1,"TABLE_END"):
                    print("found table end...")
                    print("now we check for rows...")
                    new_lines += token_list.count_new_lines(start=results[1]+new_lines+2)

                    #normally now return the node with the childs:

                    return cNode("TABLE",results[1]+new_lines+2,childs=results[0])


                return False


            print("hi")
        else:
            print("Could not find a table")
            return False
