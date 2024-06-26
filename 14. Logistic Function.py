import math


def predict_probability(x, b0, b1):
    return 1.0 / (1.0 + math.exp(-(b0 + b1 * x)))