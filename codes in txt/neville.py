#https://github.com/gisalgs/geom/blob/master/neville.py
__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"

def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    Input
      datax: input x's in a list of size n
      datay: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
        print(p)
    return p[0]


fx = [1.0, 1.3, 1.6, 1.9]
fy = [0.7651977, 0.6200860, 0.4554022, 0.2818186]
print(neville(fx, fy, 1.5))