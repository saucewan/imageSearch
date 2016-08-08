import web
from index import Index
from upload import Upload
from searchbytag import SearchByTag
from allimg import AllImg
from addtag import AddTag

urls = (
    '/upload', 'Upload',
    '/searchbytag','SearchByTag',
    '/','Index',
    '/allimg','AllImg',
    '/addtag','AddTag',
)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()