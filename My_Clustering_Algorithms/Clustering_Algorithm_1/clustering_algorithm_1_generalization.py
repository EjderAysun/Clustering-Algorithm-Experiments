import random
import numpy
import matplotlib.pyplot as plt

def create_data(x_range_min:int, x_range_max:int, dataSize:int):
    return [random.randint(x_range_min, x_range_max) for _ in range(dataSize)]

def save_data(data:list, name:str):
    with open("My_Clustering_Algorithms/Clustering_Algorithm_1/algorithm1_generalization_data.txt", "a") as f:
        f.write(name + ": " + str(data) + "\n")

# x = data
# This algorithm only works for datasets with 2 variables (x1 and x2 variables).
def clustering_algorithm_1_generalization(x1:list, x2:list, cluster_num:int):

    massX1 = sum(x1)/len(x1)
    massX2 = sum(x2)/len(x2)

    mass = massX1+massX2
    mass_cons = mass / (cluster_num-1)

    clusters = [[[], []] for _ in range(cluster_num)]

    for i, j in zip(x1, x2):
        Sum = i + j
        if(Sum < mass_cons):
            clusters[0][0].append(i)
            clusters[0][1].append(j)
        elif(Sum >= mass):
            clusters[cluster_num-1][0].append(i)
            clusters[cluster_num-1][1].append(j)
        else:
            for k in range(1, cluster_num-1):
                if(Sum >= mass_cons*k and Sum < mass_cons*(k+1)):
                    clusters[k][0].append(i)
                    clusters[k][1].append(j)
    print(clusters)
    return clusters

def plot_graph(clusters):
    for i in clusters:
        plt.scatter(i[0], i[1], c=numpy.random.rand(3,))
    plt.show()

def t_1():

    # create three clusters that are clearly three separate clusters
    x1 = create_data(10, 30, 25)
    x1.extend(create_data(40, 55, 25))
    x1.extend(create_data(65, 85, 25))
    #x1.append(0)
    x2 = create_data(75, 90, 25)
    x2.extend(create_data(50, 65, 25))
    x2.extend(create_data(25, 40, 25))
    #x2.append(0)

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1_generalization(x1, x2, 3)
    plot_graph(clusters)

def t_2():

    # create three clusters that are clearly three separate clusters
    x1 = create_data(65, 85, 25)
    x1.extend(create_data(40, 55, 25))
    x1.extend(create_data(10, 30, 25))

    x2 = create_data(75, 90, 25)
    x2.extend(create_data(50, 65, 25))
    x2.extend(create_data(25, 40, 25))

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1_generalization(x1, x2, 3)
    plot_graph(clusters)

def t_3():

    # create random variables
    x1 = create_data(0, 100, 75)
    x2 = create_data(0, 100, 75)

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1_generalization(x1, x2, 3)
    plot_graph(clusters)

def t_4():

    # create random variables
    x1 = create_data(-100, 100, 75)
    x2 = create_data(-100, 100, 75)

    save_data(x1, "x1")
    save_data(x2, "x2")

    clusters = clustering_algorithm_1_generalization(x1, x2, 3)
    plot_graph(clusters)

def do_experiment(iter_num:int, t):
    # successful
    for i in range(iter_num): # repeat the experiment 10 times
        t()

# do_experiment(10, t_1)
# do_experiment(10, t_2)
# do_experiment(10, t_3)
# do_experiment(10, t_4)

# Results:
# The failure of the generalized algorithm is proven by the above 4 tests.
# The algorithm tends to draw only the equation x = - y + b.
# It cannot even separate 3 clearly distinct sets.
# At this point it is useless to continue improving the algorithm because the basic approach must change.