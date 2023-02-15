# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the number of experiments and measurements
Nexp = 100  # number of experiments
Nmeas = 1000  # number of measurements in each experiment

# Define the arrival rate for two different scenarios
arrival_rate_1 = 2  # average arrival rate in scenario 1
arrival_rate_2 = 4  # average arrival rate in scenario 2

# Define the name of the output file and a flag to indicate whether to write to a file
OutputFileName = "bank_queue_results.txt"
doOutputFile = True

# Load the data from the text file
data = np.loadtxt("bank_data.txt")

# Separate the data into the number of customers on each day of the week
monday_data = data[0:100]
tuesday_data = data[100:200]
wednesday_data = data[200:300]
thursday_data = data[300:400]
friday_data = data[400:500]

# Define the hypothesis: the bank has more customers on Tuesday than on other days
arrival_rate_tuesday = tuesday_data.mean()
arrival_rate_other = (monday_data.mean() + wednesday_data.mean() + thursday_data.mean() + friday_data.mean()) / 4

# Compute the likelihood for the hypothesis that the bank has more customers on Tuesday
likelihood_more_tuesday = 1
for tuesday_waiting_time in tuesday_data:
    # Multiply the Poisson probability mass function for each waiting time
    likelihood_more_tuesday *= poisson.pmf(tuesday_waiting_time, arrival_rate_tuesday)

# Compute the likelihood for the hypothesis that the bank has fewer or equal customers on Tuesday
likelihood_less_tuesday = 1
for monday_waiting_time in monday_data:
    # Multiply the Poisson probability mass function for each waiting time
    likelihood_less_tuesday *= poisson.pmf(monday_waiting_time, arrival_rate_other)
for wednesday_waiting_time in wednesday_data:
    # Multiply the Poisson probability mass function for each waiting time
    likelihood_less_tuesday *= poisson.pmf(wednesday_waiting_time, arrival_rate_other)
for thursday_waiting_time in thursday_data:
    # Multiply the Poisson probability mass function for each waiting time
    likelihood_less_tuesday *= poisson.pmf(thursday_waiting_time, arrival_rate_other)
for friday_waiting_time in friday_data:
    # Multiply the Poisson probability mass function for each waiting time
    likelihood_less_tuesday *= poisson.pmf(friday_waiting_time, arrival_rate_other)

# Compare the likelihoods and make a decision
if likelihood_more_tuesday > likelihood_less_tuesday:
    print("The hypothesis that the bank has more customers on Tuesday is supported by the data")
else:
    print
