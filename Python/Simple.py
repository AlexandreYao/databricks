# Databricks notebook source
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

train_data_length = 1024
train_data = np.zeros((train_data_length, 2))
train_data[:, 0] = 2 * math.pi * np.random.rand(train_data_length)
train_data[:, 1] = np.sin(train_data[:, 0])

# COMMAND ----------

plt.plot(train_data[:, 0], train_data[:, 1], ".")
