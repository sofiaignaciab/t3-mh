import numpy as np

def f1(x):
    return 4 - 4 * x[0]**3 - 4 * x[0] + x[1]**2

def f2(x):
    terms = [(x[i]**2) * (2**(i)) for i in range(6)]
    return (sum(terms) - 1745) / 899

def f3(x):
    return (x[0]**6 + x[1]**4 - 17)**2 + (2 * x[0] + x[1] - 4)**2

def f4(x):
    xi = np.array(x)
    if np.any(xi <= 2) or np.any(xi >= 10):
        return np.inf
    term1 = np.sum((np.log(xi - 2))**2 + (np.log(10 - xi))**2)
    term2 = (np.prod(xi))**0.2
    return term1 - term2
