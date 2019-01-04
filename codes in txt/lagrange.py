#https://gist.github.com/markwatson/960210

# the code
import functools
def lagrangian_interpolate(samples):
    """
    Takes some samples as a list of tuples and returns a function that's
    a lagrangian interpolation of all the samples.
    """
    X = 0 # the tuple index of the X variable in the samples
    Y = 1 # the tuple index of the Y variable in the samples
    n = len(samples)
    # define the L function as a function generator that generates L functions
    # for a given i
    def L(i):
        "This function generates an L function for a given x_i"
        def L_gen(x):
            ret = []
            for j in range(n):
                if j != i:
                    ret.append((x - samples[j][X])/(samples[i][X] - samples[j][X]))
            print(ret)
            return functools.reduce(lambda a,b: a*b, ret)
        return L_gen

    return lambda x: sum(L(i)(x) * samples[i][Y] for i in range(n))

            
# main
prob_1 = lagrangian_interpolate([(2,1.4142),(2.5,1.5811),(3.0,1.7321),(2.7,1.6432)])
print (prob_1(2.2),"\n")
