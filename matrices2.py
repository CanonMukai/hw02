import numpy, sys, time

f = open('time_n_kji.txt','w')

for n in range(2, 50):
    
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C
    
    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    ######
    begin = time.time()
    
    for k in range(n):
        for j in range(n):
            for i in range(n):
                c[i, j] += a[i, k] * b[k, j]

    end = time.time()
    ######
    
    calc_time = end - begin
    f.write(str(n) + ' ' + str(calc_time) + '\n')

f.close()
