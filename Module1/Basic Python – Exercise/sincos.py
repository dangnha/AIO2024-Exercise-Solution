def giaithua(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

def sin(x, n):
    result = 0
    for i in range(n):
        if i % 2 ==0:
            result += x**(i*2+1)/giaithua(i*2+1)
        else:
            result -= x**(i*2+1)/giaithua(i*2+1)
    print(result)

def cos(x, n):
    result = 0
    for i in range(n):
        if i % 2 ==0:
            result += x**(i*2)/giaithua(i*2)
        else:
            result -= x**(i*2)/giaithua(i*2)
    print(result)
    
def sinh(x, n):
    result = 0
    for i in range(n):
        result += x**(i*2+1)/giaithua(i*2+1)
    print(result)

def cosh(x, n):
    result = 0
    for i in range(n):
        result += x**(i*2)/giaithua(i*2)
    print(result)
    
# Check test case
sin(3.14, 10)
cos(3.14, 10)
sinh(3.14, 10)
cosh(3.14, 10)
    