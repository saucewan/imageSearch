import view
from view import render
import web
import csv
class AddTag:
    def GET(self):
        x=web.input()
        imgpath=x.imgpath
        taglist=[]
        print imgpath
        with open('tag.csv') as f:
            reader=csv.reader(f)
            for row in reader:
                temppath=row[0].replace('\\','/')
                print temppath
                if imgpath==temppath:
                    taglist=row[1:]
                    break
            f.close()
        return render.base(view.addtag(imgpath,taglist))
        
       
    def POST(self):
        x=web.input()
        newtag=x['newtag']
        imgpath=x['imgpath']
        f=open('tag.csv','r')
        reader=csv.reader(f)
        templist=[row for row in reader]
        find=False
        for row in templist:
            if row[0].replace('\\','/')==imgpath:
                row.append(newtag)
                find=True
                break
        if find==False:
            templist.append([imgpath,newtag])
        f.close()
        f=open('tag.csv', 'w')
        writer=csv.writer(f)
        writer.writerows(templist)
        f.close()
        raise web.seeother('/addtag?imgpath='+imgpath)