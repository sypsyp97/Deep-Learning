import copy
import numpy as np
from Layers import *
from Optimization import *


class NeuralNetwork:

    # constructor
    def __init__(self, optimizer, weights_initializer, bias_initializer):

        # create public members
        self.loss = []
        self.layers = []
        self.data_layer = None
        self.loss_layer = None

        # store training data
        self.input = None
        self.label = None
        self.input_dim = 0
        self.optimizer = optimizer

        self.weights_initializer = weights_initializer
        self.bias_initializer = bias_initializer

    def forward(self):
        # training data
        self.input, self.label = self.data_layer.forward()
        input_tensor = self.input

        # traverse every layer
        for layer in self.layers:
            # output of the former layer = input of the next layer
            input_tensor = layer.forward(input_tensor)

        out = self.loss_layer.forward(input_tensor, self.label)

        return out

    def backward(self):
        # backpropagation from Loss layer
        error = self.loss_layer.backward(self.label)

        # backpropagation for every layer from back to front
        for layer in self.layers[::-1]:
            error = layer.backward(error)

        return error

    def append_trainable_layer(self, layer):
        optimizer = copy.deepcopy(self.optimizer)

        # set optimizer for the layer
        layer.optimizer = optimizer
        layer.initialize(self.weights_initializer, self.bias_initializer)

        # append the layer to layers
        self.layers.append(layer)

    def train(self, iterations):
        for epoch in range(iterations):
            print("training  ", epoch, " of ", iterations)
            # store loss for each iteration
            self.loss.append(self.forward())
            self.backward()

    def test(self, input_tensor):
        for layer in self.layers:
            input_tensor = layer.forward(input_tensor)
        y_pred = input_tensor
        return y_pred









