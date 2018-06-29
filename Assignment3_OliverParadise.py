

# Question 1
def trace(aa):
    s = 0
    for i in range(len(aa)):
        s = s + aa[i][i]
    return s

# Question 2
def minor(aa,i,j):
    m = []
    for p in range(len(aa)):
        if p != i-1:
            m.append(aa[p][:j-1] + aa[p][j:])
    return m

# Question 3
def detc(aa):
    if len(aa) == 1:
        return aa[0][0]
    if len(aa) == 2:
        return aa[0][0]*aa[1][1]-aa[0][1]*aa[1][0]
    else:
        return sum((-1)**(j+1)*aa[0][j-1]*detc(minor(aa,1,j)) for j in range(1,len(aa)+1))

# Question 4
def matmul(aa,bb): 
   nrow,nk,ncol = len(aa),len(aa[0]),len(bb[0])
   ab = [[0.0 for j in range(ncol)] for i in range(nrow)]
   for i in range(nrow):
      for j in range(ncol):
         ab[i][j] = sum([aa[i][k]*bb[k][j] for k in range(nk)])
   return ab

def matsum(aa,bb):
   nrow,ncol = len(aa),len(aa[0])
   ab = [[0.0 for j in range(ncol)] for i in range(nrow)]
   for i in range(nrow):
      for j in range(ncol):
         ab[i][j] = aa[i][j] + bb[i][j]
   return ab

def ident(n): # Returns the identity matrix of dimension n
    m = [[0.0 for j in range(n)] for i in range(n)]
    for i in range(n):
        m[i][i] = 1.0
    return m

def matpower(aa,n): # Finds (aa)^n
    m = ident(len(aa))
    for i in range(n):
        m = matmul(m,aa)
    return m

def matscal(aa,n): # Multiplies square matrix, aa, by a scalar, n
    i = []
    for p in range(len(aa)):
        j = []
        for q in range(len(aa)):
            j.append(n*aa[p][q])
        i.append(j)
    return i

def factorial(n): # Finds n!
    m = n
    i = 1
    while i != n:
        m = m*(n-i)
        i = i+1
    return m    

def matexp(aa,n=9):
    s = ident(len(aa))
    for p in range(1,n+1):
        s = matsum(s,matscal(matpower(aa,p),1/factorial(p)))
    return s

# Question 5

def matnorm(aa): # Finds the matrix norm of aa
    s = 0
    for i in range(len(aa)):
        for j in range(len(aa)):
            s = s + abs(aa[i][j])
    return s

def matsub(aa,bb): # Subtracts matrix bb from matrix aa
   nrow,ncol = len(aa),len(aa[0])
   ab = [[0.0 for j in range(ncol)] for i in range(nrow)]
   for i in range(nrow):
      for j in range(ncol):
         ab[i][j] = aa[i][j] - bb[i][j]
   return ab

def matinv(aa,eps=1e-15,maxit=20,xx0=None):
    if xx0 == None:
        xx = ident(len(aa))
    else:
        xx = xx0
    n = 0
    while matnorm(matsub(matmul(aa,xx),ident(len(aa)))) > eps:
        xx = matsub(matscal(xx,2),matmul(xx,matmul(aa,xx)))
        n = n + 1
        if n > maxit:
            print("Error: Matrix did not converge to its inverse within", maxit, "iterations")
            raise
    return xx

# Question 6

from poly2 import *

def pident(n): # Returns the identity matrix of dimension n
    m = [[Poly(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        m[i][i] = Poly(1)
    return m

def pmatsub(aa,bb): # Subtracts matrix bb from matrix aa
   nrow,ncol = len(aa),len(aa[0])
   ab = [[Poly(0.0) for j in range(ncol)] for i in range(nrow)]
   for i in range(nrow):
      for j in range(ncol):
         ab[i][j] = aa[i][j] - bb[i][j]
   return ab

def psum(a): # Returns the sum of a list of Polys, used in pmatmul below
   s = Poly(0)
   for i in a:
      s = s + i
   return s

def pmatmul(aa,bb):
   nrow,nk,ncol = len(aa),len(aa[0]),len(bb[0])
   ab = [[Poly(0.0) for j in range(ncol)] for i in range(nrow)]
   for i in range(nrow):
      for j in range(ncol):
         ab[i][j] = psum([aa[i][k]*bb[k][j] for k in range(nk)])
   return ab

def pmatinv(aa,niter=2,xx0=None):
   if xx0 == None:
      xx = pident(len(aa))
   else:
      xx = xx0
   n = 0
   while niter < 2:
      xx = pmatsub(matscal(xx,2),pmatmul(xx,pmatmul(aa,xx)))
      n = n + 1
   return xx
