

from tokenizer.tokenizer import cTokenizer
from content_parser.cont_parser import cContextParser
from tabelizer.cTabelizer import  cTabelizer

class LuaParser():
    def __init__(self):
        pass



    def __parse_file(self,path):
        #start with tokenizer to find parts:
        pass

    def readFile(self,path):
        pass

    def readFilesFromPath(self,path):
        pass


    def test(self,txt):
        tokenizer=cTokenizer().tokenize(txt)
        context_parsed =cContextParser().parse(tokenizer)
        cTabelizer().parse(context_parsed[0][0])






parser=LuaParser()
parser.test("""local template_mob ={
                name="Goblin",
                
                hp = 19,
                exp = 10,
                power = 3,
                def = 0,
                
                ai = "BasicMonster",
                tile = 0,
                
                chances={
                    {80,1},
                    {50,2},
                    {30,3},
                    {15,4},
                    {3,5},
                    {0,7}
                },
                
                color ="darker_green",
                blocking = true,
                render = RenderOrder.ACTOR
                
            }
            
            
            return template_mob
            """
            )


