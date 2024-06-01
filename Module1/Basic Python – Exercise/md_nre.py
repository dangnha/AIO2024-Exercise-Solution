def MD_nRE(y, y_hat, n, p):
    result = (y**(1/n) - y_hat**(1/n))**p
    print(result)
# Check test case
MD_nRE(100, 99.5, 2, 1)
MD_nRE(50, 49.5, 2, 1)
MD_nRE(20, 19.5, 2, 1)
MD_nRE(0.6, 0.1, 2, 1)