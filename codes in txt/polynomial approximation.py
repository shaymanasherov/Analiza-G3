
def polynomial_approximation(fx, fy):
    A = []
    n = len(fx)

    for i in range(n):
        A.append([fx[i]**2, fx[i], 1, fy[i]])
    return A

x = [1, 3, 5]
y = [10.5, 6.1, 3.5]
print(polynomial_approximation(x,y))
#ariel goeta ©.