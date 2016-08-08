import web
import cv2


t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=False, 
    globals=t_globals)
render._keywords['globals']['render'] = render

def displayresult(results):
    return render.items(results)
def tagresult(tag,results):
    return render.tagresult(tag,results)
def imgresult(img,results):
    return render.imgresult(img,results)
def noresult():
    return render.noresult()
    
def uploadpage():
    return render.uploadcontrol()

def searchbytagpage():
    return render.searchbytagcontrol()

def index():
    return render.index()

def allimg(imglist):
    return render.items(imglist)

def addtag(imgpath,taglist):
    return render.addtag(imgpath,taglist)