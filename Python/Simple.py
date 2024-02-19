# Databricks notebook source
import numpy as np
import matplotlib.pyplot as plt
nb = 1024
data = np.zeros((nb, 2))
data[:, 0] = 2 * np.pi * np.random.rand(nb)
data[:, 1] = np.sin(data[:, 0])
plt.plot(data[:, 0], data[:, 1], ".")
