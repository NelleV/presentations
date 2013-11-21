from os import path

filename = path.abspath(__file__)
print filename
print path.dirname(filename), "+", path.basename(filename)
print "Is a dir?", path.isdir(filename)
print "Is a file?", path.isfile(filename)
