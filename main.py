r1 = int(input()) 
c1 = int(input())

r2 = int(input())
c2 = int(input())

if (c1 == r2) :
    mat1 = [[int(input()) for i in range(c1)] for j in range(r1)] 
    mat2 = [[int(input()) for i in range(c2)] for j in range(r2)]

    matrix = [[0] * r1 for i in range(c2)]
    for i in range(r1) :
        for j in range(c2) :
            for k in range(c1) :
                matrix[i][j] += mat1[i][k] * mat2[k][j] 

    for i in matrix :
        print(i)

else :
    print('Not possible')


