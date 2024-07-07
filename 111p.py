
import numpy as np
import matplotlib.pyplot as plt


def getDataSource(data_path):
    temperature = []
    ice_cream_sales = []

    with open(data_path, 'r') as file:
        next(file)
        for line in file:
            temp, sales = line.strip().split(',')
            temperature.append(float(temp))
            ice_cream_sales.append(float(sales))

    return np.array(temperature), np.array(ice_cream_sales)


def findCorrelation(temp, sales):
    correlation_matrix = np.corrcoef(temp, sales)
    correlation = correlation_matrix[0, 1]
    return correlation


def plotFigure(data_path):
    temp, sales = getDataSource(data_path)
    plt.scatter(temp, sales, color='b')
    plt.xlabel('Temperature')
    plt.ylabel('Ice Cream Sales')
    plt.title('Temperature vs Ice Cream Sales')
    plt.show()


def setup(data_path):
    temp, sales = getDataSource(data_path)
    correlation = findCorrelation(temp, sales)
    print(f"The correlation between temperature and ice cream sales is {correlation:.2f}")
    plotFigure(data_path)


