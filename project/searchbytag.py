import view
import web
from view import render
from search import Search
from global_mod import Global_Mod

class SearchByTag:
    def GET(self):
        return render.base(view.searchbytagpage())
        #return render.base("<img src='./static/sheep.png'>")
        
        
        
    def POST(self):
        x = web.input(querytag='')
        gm=Global_Mod()
        gm.tag=x.querytag
        gm.results=Search.searchbytag(gm.tag)
        gm.results=[item.replace('\\','/') for item in gm.results]
        print gm.results
        if gm.results==[]:
            return render.base(view.noresult())
        else:
            return render.base(view.tagresult(gm.tag,gm.results))