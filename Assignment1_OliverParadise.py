# I confirm that this is my own work done without the help of other
# people. I did not consult books, the internet or sources other
# than the course notes and handouts, and the Python documentation.

def esix(x,y):                          
    return((x**6+y**6)**(1/6))


def true2(p,q,r,s):
    t = []
    for i in (p,q,r,s):
        if (i == True):
            t.append(i)
    if (len(t) == 2):
        return(True)
    else:
        return(False)


def primepi(n):
    notPrimeCounter = 0
    for i in range(1,n+1):
        if (i == 1):
                notPrimeCounter = notPrimeCounter + 1
        for j in range(2,int(i**0.5)+1): 
            if (i%j == 0):
                notPrimeCounter = notPrimeCounter + 1
                break
    return((n-notPrimeCounter)/n)


def amean(x):
    add = 0
    for i in range(len(x)):
        add = add + x[i]
    return(add/len(x))

def gmean(x):
    multiply = 1
    for i in range(len(x)):
        multiply = multiply * x[i]
    return(multiply**(1/len(x)))

def hmean(x):
    recipSum = 0
    for i in range(len(x)):
        recipSum = recipSum + (1/x[i])
    divided = recipSum / len(x)
    return(divided**-1)


def expform(x):
    y = 0
    m = 0
    if (abs(x)<1):
        while (abs(x)<1):
            x = x * 10
            m = m - 1
        y = x
    else:
        while (abs(x)>=10):
            x = x / 10
            m = m + 1
        y = x
    return(y,m)
