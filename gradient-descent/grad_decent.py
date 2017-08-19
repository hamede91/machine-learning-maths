from numpy import *


def main():
    #load the data
    points = genfromtxt('data.csv', delimiter=",")

    #initialize slope, intercept
    b_init = 0
    m_init = 0
    #number of iterations
    iterations = 1000

    #hyperparameters
    learning_rate = 0.0001
    # [b, m] = gradient_descent()

if __name__ == '__main__':
    main()
