import itertools as it

def interpolate_vertical(x1,y1,x2,y2,n) :
    ov = sorted([[y1,x1],[y2,x2]])
    new_ys = np.linspace(ov[0][0], ov[1][0], num=n)
    new_xs = np.interp(new_ys,[ov[0][0],ov[1][0]],[ov[0][1],ov[1][1]])
    vertices = list(zip(new_xs,new_ys))
    return vertices if y1 < y2 else list(reversed(vertices))

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)
