from glob import glob

filenames = glob("*")
for filename in filenames:
    if filename.endswith(".py"):
        print "Python file !"
    else:
        print "Not python file :("
