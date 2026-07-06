"""Classes and functions for working with Multilayer Perceptrons
Hopefully generalizable too.
Version: 0.0.0"""
import numpy

class network:
    def __init__(self, weights, input_length, hidden_length, hidden_count, output_length):
        # weights is both weights and biases
        self.weightCount = (input_length*hidden_length) + hidden_length #weights + biases
        self.weightCount += ((hidden_length**2)*(hidden_count-1)) + (hidden_length*(hidden_count-1))
        self.weightCount += (hidden_length*output_length) + output_length