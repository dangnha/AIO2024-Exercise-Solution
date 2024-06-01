import math
import math

def Sigmoid(x):
    return 1/(1+math.exp(-x))

def ReLU(x):
    return max(0,x)

def ELU(x):
    return x if x>0 else 0.01 * (math.exp(x)-1)

def activation(x, f):
    if not isinstance(x, (int, float)):
        print("x must be a number")
        return
    x = float(x)
    
    if f == "sigmoid":
        print(Sigmoid(x))
    elif f == "relu":
        print(ReLU(x))
    elif f == "elu":
        print(ELU(x))
    else:
        print("Unknown activation function")
        
# Check test case
activation(1, "sigmoid")
activation(1, "relu")
activation(1, "elu")
activation("a", "elu")
activation(1, "tanh")
activation(1, 1)