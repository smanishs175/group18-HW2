import src.utils
import src.num
import src.sym
import re

class Cols:

    def __init__(self,names):
        self.names=names
        self.all= []
        self.klass=None
        self.x= []
        self.y=[]

        for c,s in names.items():

            start_Caps = re.search(r'^[A-Z]*',s)
            ## if starts with Uppercase
            if start_Caps:
                obj=num.Num(c,s)
            else:
                obj = sym.Sym(c,s)

            col = utils.push(self.all,obj)

            ## ends with :
            ends_with_colon = re.search(r':$',s)
            ## ends with !
            ends_with_exc = re.search(r'!$',s)
            ## contains ! or + or -
            signs_present = re.search(r'[!+-]',s)

            if not ends_with_colon:
                if signs_present:
                    utils.push(self.x,col)
                else:
                    utils.push(self.y, col)

                if ends_with_exc:
                    self.klass = col


