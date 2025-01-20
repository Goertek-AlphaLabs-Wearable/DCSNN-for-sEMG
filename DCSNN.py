import snntorch as snn
import torch
import torch.nn as nn
from snntorch import surrogate
import numpy as np

# Define Network
spike_grad = surrogate.fast_sigmoid(slope=25)
beta = 0.5


class DCSNN(nn.Module):
    def __init__(self, SNN_neurons=[64, 32], hidden_layers_num=2, population_num=50,
                 num_output_neuron=6, channel_num = 8, trains_num = 10, action_duration=300, window_length = 20):
        super().__init__()
        self.channel_num = channel_num
        self.trains_num = trains_num
        self.action_duration = action_duration
        self.window_length = window_length
        self.num_input_neuron = self.action_duration / self.window_length
        self.SNN_neurons = SNN_neurons
        self.hidden_layers_num = hidden_layers_num
        self.population_num = population_num
        self.num_output_neuron = num_output_neuron

        # Initialize layers
        self.layers = nn.ModuleList()
        # input layer
        self.layers.append(nn.Linear(self.num_input_neuron, self.SNN_neuron[0]))
        self.layers.append(snn.Leaky(beta=beta, spike_grad=spike_grad, init_hidden=True))
        # hidden layers
        for i in range(self.hidden_layers_num):
            self.layers.append(nn.Linear(self.SNN_neuron[i], self.SNN_neuron[i + 1]))
            self.layers.append(snn.Leaky(beta=beta, spike_grad=spike_grad, init_hidden=True))
        # output layers
        self.layers.append(
            nn.Linear(self.SNN_neuron[self.hidden_layers_num - 1], self.num_output_neuron * self.population_num))
        self.layers.append(snn.Leaky(beta=beta, spike_grad=spike_grad, init_hidden=True))
        self.model = nn.Sequential(*self.hidden_layers)

    def multi_trains_additive_solver(self, x):
        x = torch.sum(x, dim=1)
        return x

    def multi_steps_additive_solver(self, x):
        x = x.unfold(dimension=2, size=self.window_length, step=self.window_length)
        x = x.sum(dim=-1)
        return x

    def forward(self, x):
        # x: shape [B*C*N*T]
        x = self.multi_trains_additive_solver(x)
        x = self.multi_steps_additive_solver(x)
        return self.model(x)
