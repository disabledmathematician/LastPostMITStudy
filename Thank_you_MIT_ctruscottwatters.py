# -*- coding: utf-8 -*-
"""
Charles Thomas Wallace Truscott
127 Broken Head Rd Suffolk Park 2481

Basic Demonstration of what is learnt at MIT in 6.0001 and 6.0002
"""
import numpy as np
import math
import random

class MITStat(object):
    def __init__(self, x_vals):
        self.x = x_vals
        
    def mean(self):
        # Charles Thomas Wallace Truscott. Thank you MIT
        return sum(self.x) / len(self.x)
    def sqrt(self, n):
        # Thank you John Guttag, Eric Grimson and Ana Bell and the MIT Faculty
        high = n
        low = 0
        guess = (high + low) / 2.0
        while (abs(round((guess ** 2 - n), 6)) > 0.000001):
            print("Guess: {}, High: {}, Low: {}".format(guess, high, low))
            print("Guess ^ 2: {}, n: {}".format(guess ** 2, n))
            if (guess ** 2 > n):
                high = guess
                guess = (high + low) / 2.0
            if (guess ** 2 < n):
                low = guess
                guess = (high + low) / 2.0
        # Thank you edX.org
        print("Guess Squared is {} and n is: {}".format(guess ** 2, n))
        return guess
    def variance(self):
        t = self.x
        L = []
        for e in t:
            L.append(self.mean())
        R = []
        c = 0
        while (c < len(L) and c < len(self.x)):
            R.append((self.x[c] - L[c]) ** 2)
            c += 1
        return sum(R) / len(self.x)
    
    def stddev(self):
        return np.sqrt(self.variance())
    
    def coefficient_of_variation(self):
        return self.stddev(self.x) / self.mean(self.x)
    
    def normal_distribution(self):
        L = []
        R = []
        for elem in self.x:
            R.append((1 / (self.stddev() * self.sqrt(2 * np.pi)) * np.e ** (-((elem - self.mean()) / (2 * self.stddev()) ** 2))))
        return R
    def geometric_distribution(self):
        L = []
        for elem in self.x:
            L.append(((1 - elem) ** ((1)/(len(self.x)))) * elem)
        return L
    def binomial_distribution(self):
        L = []
        bincoeff = math.factorial(len(self.x)) / math.factorial(len(self.x)) * math.factorial(len(self.x) - len(self.x))
        for elem in self.x:
            L.append(bincoeff * (elem ** len(self.x)) *  (1 - elem) ** (len(self.x) - len(self.x)))
        return L
def CharlesTruscott():
    # I love you Alison Thompson OAM
    # I love you Dad, Mark William Watters and Uncle Rodney
    L = [n for n in range(0, 11, 1)]
    R = [random.choice(L) for n in range(1, 101)]
    n = MITStat(R)
    mean = n.mean()
    variance = n.variance()
    stddev = n.stddev()
    import matplotlib.pyplot as plt
#    plt.figure(0, dpi=600, figsize=[8, 8])
    x1 = [a for a in range(len(R))]
#    y1 = R
#    plt.plot(x1, y1)
#    plt.show()
    plt.figure(1, dpi=600, figsize=[8, 8])
    x2 = x1
    y2 = n.normal_distribution()
    plt.title("Charles Truscott Watters. Normal Distribution of Randomly Generated Data")
    plt.hist(y2, bins=20, histtype='bar', cumulative=True, align='mid', color='pink', edgecolor='black')
    plt.savefig('1.png')
    x3 = x1
    y3 = n.geometric_distribution()
    plt.figure(2, dpi=600, figsize=[8, 8])
    plt.title("Charles Truscott Watters. Geometric Distribution of Randomly Generated Data")
    plt.hist(y3, histtype='bar', cumulative=True, align='mid', color='crimson', edgecolor='black')
    plt.savefig('2.png')
    x4 = x1
    y4 = n.binomial_distribution()
    plt.figure(3, dpi=600, figsize=[8, 8])
    plt.title("Charles Truscott Watters. Binomial Distribution of Randomly Generated Data, where n = k")
    plt.hist(y4, histtype='bar', cumulative=True, align='mid', color='crimson', edgecolor='black')
    plt.savefig('3.png')
#    plt.figure(2, dpi=600, figsize=[8, 8])
#    plt.plot(x2, y2)
#    plt.show()
    return 0

if __name__ == """__main__""": CharlesTruscott()
        
