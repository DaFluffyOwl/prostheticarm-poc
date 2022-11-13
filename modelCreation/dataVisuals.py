import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv("fullDataset.csv")
dataset.plot.bar(x = 'handstate', y = 'values')
plt.show()