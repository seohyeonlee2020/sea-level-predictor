import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    scatter_df = df[['Year', 'CSIRO Adjusted Sea Level']]
    #no null values
    scatter_df.isna().any()
    x = scatter_df['Year']
    y=scatter_df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize = (12, 8))
    ax = plt.scatter(x, y)

    # Create first line of best fit
    results = linregress(x, y)
    extrap_x = range(x[0], 2051, 1)
    ax = plt.plot(range(x[0], 2051, 1), results.intercept + results.slope*extrap_x, 'r', label='fitted line')

    
    data_since_2000 = df[df['Year'] >= 2000]
    data_since_2000.head()
    x_since_2000 = data_since_2000['Year']
    y_since_2000 = data_since_2000['CSIRO Adjusted Sea Level']
    results_since_2000 = linregress(x_since_2000, y_since_2000)
    extrap_x2 = range(2000, 2051, 1)
    print(extrap_x2)
    ax = plt.plot(extrap_x2, results_since_2000.intercept + results_since_2000.slope*extrap_x2, 'b', label='fitted line 2')
    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()