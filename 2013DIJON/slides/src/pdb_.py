def function_to_debug(x, y):
    if x < y:
        print "x smaller than y"
    elif x == y:
        print "x equal y"
    else:
        import pdb; pdb.set_trace()
        print "x bigger than y"
