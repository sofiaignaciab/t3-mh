import math
import numpy as np

def f4(x):
    sum_terms = sum(
        (math.log(xi - 2))**2 + (math.log(10 - xi))**2
        for xi in x
    )
    product_term = np.prod(x)**0.2
    return sum_terms - product_term