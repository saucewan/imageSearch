import web
from colordescriptor import ColorDescriptor
from searcher import Searcher
from search import Search
import cv2
import numpy
import view
from view import render
from global_mod import Global_Mod

class Upload:
    def GET(self):
        return render.base(view.uploadpage())

    def POST(self):
        x = web.input(myfile={})

        print x['myfile'].filename
        gm=Global_Mod()
        gm.img = cv2.imdecode(numpy.fromstring(x['myfile'].file.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        resultslist=Search.search(gm.img)
        for row in resultslist:
            temp=list(row)
            gm.results.append(temp[1].replace('\\','/'))
        print gm.results        
        return render.base(view.imgresult(gm.img,gm.results))





        

