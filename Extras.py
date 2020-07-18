import random
import os
import recorder as l
import webbrowser
from time import *
def remover(self,file):
    os.remove(file)
class Generator:
    def generator(self):
        string = "audio-"
        for i in range(5):
            r = random.randint(0,1000000)
            string += str(r)
        return string


class Extra_fun:
    def time(self):
        return ctime()


    def websearch(self):
        # search = l.Listner().listen("Here Is What I found For You")
        search = "dogs"
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Here Is What I Found For " + search)
# print(Extra_fun().time())

