import random
import matplotlib.pyplot as plt

def create_data(x_range_min:int, x_range_max:int, dataSize:int):
    return [random.randint(x_range_min, x_range_max) for _ in range(dataSize)]

def save_data(data:list, name:str):
    with open("My_Clustering_Algorithms/Clustering_Algorithm_1/algorithm1_data.txt", "a") as f:
        f.write(name + ": " + str(data) + "\n")

# x = data
# This algorithm only works for datasets with 2 variables (x1 and x2 variables).
def clustering_algorithm_1(x1:list, x2:list):

    massX1 = sum(x1)/len(x1)
    massX2 = sum(x2)/len(x2)

    mass = massX1+massX2

    # A and B are clusters
    Ax1 = []
    Ax2 = []
    Bx1 = []
    Bx2 = []

    for i, j in zip(x1, x2):
        Sum = i + j
        if Sum <= mass:
            Ax1.append(i)
            Ax2.append(j)
        else:
            Bx1.append(i)
            Bx2.append(j)

    return [[Ax1, Ax2], [Bx1, Bx2]]

def plot_graph(clusters):
    plt.scatter(clusters[0][0], clusters[0][1], color='red') # cluster 1
    plt.scatter(clusters[1][0], clusters[1][1], color='green') # cluster 2
    plt.show()

def t_1():

    # create two clusters that are clearly two separate clusters
    x1 = create_data(20, 30, 25)
    x1.extend(create_data(60,80,25))
    x2 = create_data(30,45,25)
    x2.extend(create_data(20,45,25))

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1(x1, x2)
    plot_graph(clusters)

# the clusters are clearly separate but closer to each other than the clusters at t_1
def t_2():

    # create two clusters that are clearly two separate clusters
    x1 = create_data(20, 30, 25)
    x1.extend(create_data(35,50,25))
    x2 = create_data(30,45,25)
    x2.extend(create_data(20,45,25))

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1(x1, x2)
    plot_graph(clusters)

def t_3():

    # create random variables
    x1 = create_data(0, 100, 50)
    x2 = create_data(0, 100, 50)

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1(x1, x2)
    plot_graph(clusters)

def t_4():

    # create random variables
    x1 = create_data(10, 30, 25)
    x1.extend(create_data(40, 55, 25))
    x1.extend(create_data(65, 85, 25))
    x2 = create_data(25, 40, 25)
    x2.extend(create_data(50, 65, 25))
    x2.extend(create_data(75, 90, 25))

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1(x1, x2)
    plot_graph(clusters)

def t_5():

    # create random variables
    x1 = create_data(10, 30, 25)
    x1.extend(create_data(40, 55, 25))
    x1.extend(create_data(65, 85, 25))
    x2 = create_data(75, 90, 25)
    x2.extend(create_data(50, 65, 25))
    x2.extend(create_data(25, 40, 25))

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1(x1, x2)
    plot_graph(clusters)

def do_experiment(iter_num:int, t):
    # successful
    for i in range(iter_num): # repeat the experiment 10 times
        t()

# do_experiment(10, t_1)
# do_experiment(10, t_2)
# do_experiment(10, t_3)
# do_experiment(10, t_4)
# do_experiment(10, t_5)

# Results:
# When this algorithm is used to partition 2-variable data into 2 clusters, it tends to plot y = -x according to experiments.
# The integrations needed to measure the quality of the algorithm will be done later.