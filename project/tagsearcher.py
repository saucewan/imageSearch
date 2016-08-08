import csv
class TagSearcher:
    def __init__(self, indexPath):
        self.indexPath =indexPath
    def search(self, queryTag):
        results=[]
        with open('tag.csv') as f:
            reader=csv.reader(f)
            for row in reader:
                for tag in row[1:]:
                    if tag==queryTag:
                        results.append(row[0])
                        break
            f.close()
        return results     