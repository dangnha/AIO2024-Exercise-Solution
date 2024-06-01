def ComputeF1Score(tp, fp, fn):
    if type(tp) != int:
        print("fn mus be int")
        return
    elif type(fp) != int:
        print("fp mus be int")
        return
    elif type(fn) != int:
        print("fn mus be int")
        return    
    elif tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, fn must be greater than zero")
        return
    
    precision = tp / (tp + fp)
    print(f"Precision is: {precision}")
    recall = tp / (tp + fn)
    print(f"Recall is: {recall}")
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f"F1 score is: {f1_score}")

# Check test case
ComputeF1Score(2,3,4)
ComputeF1Score(3,4,"a")
ComputeF1Score(2,3,0)
ComputeF1Score(2.1, 3, 0)