import os
import view
from view import render
class AllImg:
    def GET(self):
        imglist=[]
        ext=['png','bmp']
        for file in os.listdir('static'):
            if file.split('.')[-1] in ext:
                imglist.append('static/'+file)
        return render.base(view.allimg(imglist))