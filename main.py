import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

if __name__ == '__main__':
    data = np.loadtxt('./data/two_var_plt.txt', delimiter=',', dtype=float)

    plt.scatter(data[:,0], data[:,1])
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(data[:, 0], data[:, 1])
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.show()

    data = np.loadtxt('./data/three_var_plt.txt', delimiter=',', dtype=float)
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

    ax = plt.figure().add_subplot(projection='3d')
    ax.scatter(data[:, 0], data[:, 1])
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.show()

    data = np.loadtxt('./data/two_var_plt.txt', delimiter=',', dtype=float)

    # ax = sns.heatmap(data, linewidth=0.5, cmap='coolwarm')
    #
    # plt.title("2-D Heat Map")
    #plt.show()

    # data = np.loadtxt('./data/three_var_plt.txt', delimiter=',', dtype=float)
    # ax = sns.heatmap(data, linewidth=0.5, cmap='coolwarm')
    #
    # plt.title("2-D Heat Map")
    # plt.show()

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.set_xlabel('Features')
    ax.boxplot(data)

    plt.show()

    fig = plt.figure()
    gs = fig.add_gridspec(1, 2)

    ax = fig.add_subplot(gs[0, 0])
    ax.hist(data[:, 0], bins=97)
    ax.set_title('Feature-1 Value Histogram')
    ax.set_xlabel('Feature-1 values')
    ax.set_ylabel('Number of occurrences in the dataset')
    ax1 = fig.add_subplot(gs[0, 1])
    ax1.hist(data[:, 1], bins=97)
    ax1.set_title('Feature-2 Value Histogram')
    ax1.set_xlabel('Feature-2 values')
    ax1.set_ylabel('Number of occurrences in the dataset')

    plt.suptitle('Histogram plot for our example with two features')
    plt.show()