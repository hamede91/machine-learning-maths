from __future__ import print_function
import matplotlib.pyplot as plt
from numpy import *

def compute_error(b, m, points):
    sum_squared_error = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        sum_squared_error += (1/N) * (y - ((m * x) + b)) **2
    return sum_squared_error / float(len(points))

def gradient_step(current_b, current_m, learning_rate, iterations, points):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))

    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += (-2/N) * (y - ((current_m * x) + current_b))
        m_gradient += (-2/N) * x * (y - ((current_m * x) + current_b))

    #update b and m
    new_b = current_b - (learning_rate * b_gradient)
    new_m = current_m - (learning_rate * m_gradient)

    return [new_b, new_m]


def gradient_descent(initial_b, initial_m, learning_rate, iterations, points):
    b = initial_b
    m = initial_m

    for i in range(0, iterations):
        b, m = gradient_step(b, m, learning_rate, iterations, array(points))
    return [b, m]


def main():
    #load the data
    points = genfromtxt('data.csv', delimiter=",")

    #initialize slope, intercept
    b_init = 0
    m_init = 0
    #number of iterations
    num_iterations = 1000

    #learning rate
    learning_rate = 0.0001

    print("Startin gradient descent at b = {}, m = {}, error = {}".format(b_init, m_init, compute_error(b_init, m_init, points)))
    print("Running...")
    [b, m] = gradient_descent(b_init, m_init, learning_rate, num_iterations, points)
    print("After {} iterations, b = {}, m = {}, error = {}".format(num_iterations, b, m, compute_error(b, m, points)))

    #plot line of best fit
    plt.figure(2)
    plt.plot(points[:, 0], points[:, 1], 'bo', label = "Training data")
    x_points = arange(0, 130)
    y_points = m * x_points + b
    plt.plot(x_points, y_points, label="Line of best fit")
    plt.xlabel("x values")
    plt.ylabel("y values")

    plt.title("Gradient descent")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
