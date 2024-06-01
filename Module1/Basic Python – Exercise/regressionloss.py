import numpy as np

def MSE(y, y_hat):
    print(f"Loss: {(y - y_hat) ** 2}")

def MAE(y, y_hat):
    print(f"Loss: {np.abs(y - y_hat)}")

def RMSE(y, y_hat):
    print(f"Loss: {np.sqrt((y - y_hat) ** 2)}")

def regressionLoss(n, name):
    y = np.random.rand(n)
    print(y)
    y_hat = np.random.rand(n)
    
    print(f"Loss name: {name}")
    print(f"Sample: {list(zip(y, y_hat))}")

    
    if name == "MSE":
        for i in range(n):
            print(f"Sample {i}")
            print(f"Predict: {y[i]}")
            print(f"Target: {y_hat[i]}")
            MSE(y[i], y_hat[i])
            print("-----------------------")
        print("=========================")
    elif name == "MAE":
        for i in range(n):
            print(f"Sample {i}")
            print(f"Predict: {y[i]}")
            print(f"Target: {y_hat[i]}")
            MAE(y[i], y_hat[i])
            print("-----------------------")
        print("=========================")
    elif name == "RMSE":
        for i in range(n):
            print(f"Sample {i}")
            print(f"Predict: {y[i]}")
            print(f"Target: {y_hat[i]}")
            RMSE(y[i], y_hat[i])
            print("-----------------------")
        print("=========================")
    
# Check test case
regressionLoss(3, "MSE")
regressionLoss(3, "MAE")
regressionLoss(3, "RMSE")
