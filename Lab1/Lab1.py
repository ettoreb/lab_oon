#
# Lab 1 - software abstraction of a network
#

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

# Signal information (signal_power, noise_power, latency, path )

# @property is a decorator

class Signal_information:
    def __init__(self, signal_power, noise_power, latency, path):
        self._signal_power = signal_power
        self._noise_power = noise_power
        self._latency = 0
        self._path = 0
# initializes latency and path to 0
# latency is total time delay due to the signal propagation
# through any network element along the path

    @property
    def signal_power(self):
        return self._signal_power

    @property
    def noise_power(self):
        return self._noise_power

    @noise_power.setter
    def set_noise_power(self, noise_power):
        self._noise_power = noise_power

    @property
    def latency(self):
        return self._latency

    @latency.setter
    def set_latency(self, latency):
        self._latency = latency

    @property
    def path(self):
        return self._path

    @path.setter
    def set_path(self, path):
        self._path = path

