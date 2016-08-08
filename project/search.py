# import the necessary packages
from colordescriptor import ColorDescriptor
from tagsearcher import TagSearcher
from searcher import Searcher

import cv2
class Search:
    @staticmethod
    def search(img):

        # initialize the image descriptor
        cd = ColorDescriptor((8, 12, 3))

        # load the query image and describe it
        #query = cv2.imread(args["query"])
        #query = cv2.imread("queries/2.png")

        features = cd.describe(img)

        # perform the search

        searcher = Searcher("feature.csv")

        results = searcher.search(features)
        return results

    @staticmethod
    def searchbytag(querytag):
        searcher = TagSearcher("tag.csv")
        results =searcher.search(querytag)
        return results
 
