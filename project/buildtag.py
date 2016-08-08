

output = open('tag.csv', "a")
output.write("%s,%s\n" % ('test3.jpg', ",".join(['tag5','tag2','tag3'])))
output.close()