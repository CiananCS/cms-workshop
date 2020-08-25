import numpy
import os
import argparse
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help="The filepath to the file to be analyzed.")
    parser.add_argument("--make_plots", help="Makes a plot of the energy", default=0)
    args = parser.parse_args() ## these are the actual arguments of our function

    ## The :-6 business omits the .mdout from the name
    newFile = open(F'{args.path[:-6]}_Etot.txt','w+')
    with open(args.path,'r') as outfile:
        data = outfile.readlines()

    Y = []
    for lines in data:
        if 'A V E R A G E S' in lines:
            break
        if 'Etot' in lines:
            words = lines.split()
            newFile.write('{}\n'.format(words[2]))
            Y.append(float(words[2]))

    newFile.close()
    Y = numpy.array(Y)
    X = numpy.linspace(1,len(Y),len(Y))
    if args.make_plots == 1:
        plt.figure()
        fig1 = plt.plot(Y, label=args.path[:-6])
        plt.xlabel('Number of Steps')
        plt.ylabel('Total Energy')
        plt.legend()
        plt.savefig('{}.png'.format(args.path[:-6]), dpi = 300)
