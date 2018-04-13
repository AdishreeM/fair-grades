import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_csv("../resources/exam.csv")
print(dataframe["math"])