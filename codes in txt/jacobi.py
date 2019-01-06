

def printAprox(arr):  # auxiliary for formatting
    for i in range(len(arr)):
        print("x%s: %.5f\t" % (i + 1, arr[i]), end=' ')
    print("\n")


def metJacobi(matrSist, arrResult, tamanh, aprox=None, maxItera=100, tolMin=1e-3):
    if aprox is None:
        aprox = [0 for i in range(tamanh)]

    aprox2 = [0 for i in range(tamanh)]
    # two vectors of approximations guarantee the iteration

    matrAum = matrSist
    arrResultAum = arrResult

    for i in range(tamanh):  #Isolates each array variable
        p = matrAum[i][i]
        for j in range(tamanh):
            if p != 0:
                matrAum[i][j] = -(matrAum[i][j] / float(p))
            if i == j:
                matrAum[i][j] = 0
        arrResultAum[i] = arrResultAum[i] / float(p)

    sucesso = False
    for x in range(maxItera):  # Calculates approximations
        print("k=%d" % (x + 1))
        if x % 2 == 0:
            for i in range(tamanh):
                soma = 0
                for j in range(tamanh):
                    soma += matrAum[i][j] * aprox[j]
                aprox2[i] = soma + arrResultAum[i]
            printAprox(aprox2)

            if (max(aprox) != 0) and \
                    (abs(max(aprox2) - max(aprox)) / abs(max(aprox))) < tolMin:
                # the tolerance has been reached
                print("O processo foi bem-sucedido")
                sucesso = True
                break

        else:
            for i in range(tamanh):
                soma = 0
                for j in range(tamanh):
                    soma += matrAum[i][j] * aprox2[j]
                aprox[i] = soma + arrResultAum[i]
            printAprox(aprox)

            if (max(aprox2) != 0) and \
                    (abs(max(aprox) - max(aprox2)) / abs(max(aprox2))) < tolMin:
                # the tolerance has been reached
                print("The process was successful")
                sucesso = True
                break

    if not sucesso:
        print("The process exceeded the maximum number of iterations")


maxItera = 3  # Maximum Iterations
tolMin = 1e-2  # Tolerance

# Para Ax = b
matriz = [[5,-1,2],  # A
          [3 ,8,-2],
          [1 ,1,4],]

arrResult = [12,-25,6]  # b

tam = len(arrResult)
aproxIni = [0 for i in range(tam)]  #Vector of initial approximations

metJacobi(matriz, arrResult, tam, aproxIni, maxItera, tolMin)

