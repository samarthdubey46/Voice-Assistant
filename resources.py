import Extras as ex
from time import ctime
import webbrowser
import recorder as l
class ho:

    def __init__(self,main,respond=None,res_fun=None):
        self.heard = main
        self.respond = respond if res_fun == None else None
        self.res_fun = res_fun
        if res_fun != None:
            self.res_fun()


ext = ex.Extra_fun()

f = ho(main="What is Your Name",respond="My Name Is PM")
s = ho(main="How Do You Do",respond="Well I Dont Do cause I'am A assistance. Dont You Do")
time = ho(main="what time is it",respond=ext.time())
exit = ho(main="exit",res_fun=exit())
search = ho("search",res_fun=ext.websearch)
# search.res_fun

z = []
z.append(f)
z.append(s)
z.append(time)
z.append(search)
z.append(exit)



