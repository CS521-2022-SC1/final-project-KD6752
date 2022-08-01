'''
July 22 Final Project Deliverable
Dan Hoogasian & Kokil Dhakal
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

# Set working directory
os.chdir('C:/Users/dhoog/Documents/MET_CS521_Summer 2022/Final_Project/final-project-KD6752/')

# Read csv data file into data frame
df = pd.read_csv("Python_project/House_Prediction_Data.csv")

# Get basic statistics on data and save as csv to current working directory
basic_stats = df.describe()
print(basic_stats)
basic_stats.to_csv('basic_stats.csv', index=False)


# Get statistics on qualitative data. Not sure what libraries would be ideal.


# Experimenting with plots from matplotlib
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.hist(df['SalePrice'], bins=40, linewidth=0.1, edgecolor="white", label="Sale Price")
ax.set(xlabel="Sale Price", ylabel="Frequency of Houses")
plt.show()