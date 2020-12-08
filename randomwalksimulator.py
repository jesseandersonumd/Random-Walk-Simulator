import numpy as np
import matplotlib.pyplot as plt

def create_random_walks(number_endpoints,number_rolls):

    '''
    Purpose: This function simulates a random walk with the number of endpoints and desired number of rolls provided. 
    Returns: A list of each individual random walk.

    '''
    walk = []

    for i in range(number_endpoints):

        random = [0]

        for x in range(number_rolls):

            check = random[-1]

            options = np.random.randint(1,7)

            if options <= 2:
                check = max(0, check - 1)
            elif options <= 5:
                check += 1
            else:
                check += np.random.randint(1,7)
            
            random.append(check)

        walk.append(random)
    
    return walk

def plots(walks):

    '''
    Purpose: To plot the random walks and to plot a histogram of the random walk data. 
    Returns: A histogram and a line plot. 

    '''
    new_array = np.array(walks)
    plt.plot(new_array)
    plt.show()
    npt = np.transpose(new_array)
    dist = npt[-1,:]
    plt.hist(dist)
    plt.show()

def main(number_endpoints,number_rolls):

    print("-----Random walk-----")
    new_walks = create_random_walks(number_endpoints,number_rolls)
    print(new_walks)
    print("-----Plots-----")
    plots(new_walks)

main(250,100)