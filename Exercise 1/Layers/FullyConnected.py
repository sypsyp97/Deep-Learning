import numpy as np
from Optimization import Optimizers


class FullyConnected:

    # constructor
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        # protected member: _optimizer
        self._optimizer = None

        self.grad_weights = None

        # w: (input_size+1, output_size)
        self.weights = np.random.uniform(0, 1, (self.input_size+1, self.output_size))

        # x:(batch_size, input_size+1)
        self.input = np.ndarray

    # property: optimizer, gradient_weights
    @property
    def optimizer(self):
        return self._optimizer

    @optimizer.setter
    def optimizer(self, new_optimizer):
        self._optimizer = new_optimizer

    @property
    def gradient_weights(self):
        return self.grad_weights

    def forward(self, input_tensor):
        # input with bias
        bias = np.ones((input_tensor.shape[0], 1))
        self.input = np.hstack((input_tensor, bias))

        out = np.dot(self.input, self.weights)
        return out

    def backward(self, error_tensor):
        # x_grad w/o bias
        weights_no_bias = self.weights[0:-1, :]
        error = np.dot(error_tensor, weights_no_bias.T)

        # w_grad
        self.grad_weights = np.dot(self.input.T, error_tensor)

        # update weights
        if self.optimizer is not None: 
            self.weights = self.optimizer.calculate_update(self.weights, self.gradient_weights)

        return error
