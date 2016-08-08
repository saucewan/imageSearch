from view import render
import view

class Index:
    def GET(self):
        return render.base(view.index())
