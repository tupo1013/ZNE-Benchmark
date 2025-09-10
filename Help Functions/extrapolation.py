import numpy as np

def polynomial_extrapolation(fold_set, fidelity_set, deg = 2):
    fit = np.polyfit(fold_set, fidelity_set, deg=deg)
    return np.polyval(fit,0)

def linear_extrapolation(fold_set, fidelity_set):
    return polynomial_extrapolation(fold_set, fidelity_set, deg = 1)

def exponential_extrapolation(fold_set, fidelity_set):
    logy = np.log(fidelity_set)
    coeffs = np.polyfit(fold_set, logy, deg=1)
    return np.exp(coeffs[1])