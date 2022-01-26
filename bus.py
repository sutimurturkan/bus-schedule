import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# Read the csv file
if os.path.exists("passengerData.csv"): 
    data = pd.read_csv("passengerData.csv")

data.head()

#Prepare data
titles = []
for column in data:
  titles.append(column)
titles.pop(0)

#Organize data by hour
da = []
for i in range(16):
  title = titles[i]
  da.append(data[title].to_numpy())


poisson_lambda = np.mean(data)
print (poisson_lambda)

days = []
for i in range(30):
  days.append(i)

for i in range(16):
  print(titles[i])
  x = da[i]
  plt.plot(days, x, 'bs')
  plt.ylabel('Number of passangers') 
  plt.xlabel('Days')
  plt.show()

from scipy.special import factorial
from scipy.stats import poisson
for i in range(16):
  print(titles[i])
  t = da[i]
  d = np.exp(-poisson_lambda[i])*np.power(poisson_lambda[i], t)/factorial(t)
  plt.plot(t, d, 'bs')
  plt.title('Poisson distribution, λ = %s' % (poisson_lambda[i]))
  plt.ylabel('P(x)') 
  plt.xlabel('k = number of occurences')
  plt.show()

for i in range(16):
  prob = poisson.cdf(10, poisson_lambda[i]) #the parameters are t, and lambda respectively
  print("The probability of 10 or less passengers at %s is: %s" % (titles[i], prob))

for i in range(16):
  prob = poisson.cdf(10, poisson_lambda[i])
  if (prob >= 0.9):
    print("%s with probability: %s" % (titles[i], prob))
