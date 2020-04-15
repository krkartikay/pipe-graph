"""
sir_model.py - simulates spread of an epidemic in a population
"""

import time
import sys

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10


# The SIR model differential equations.
def deriv(S, I, R):
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


S, I, R = S0, I0, R0

# simulation time step
dt = 1

print("Susceptible, Infected, Recovered/Removed")

while True:
    [dSdt, dIdt, dRdt] = deriv(S, I, R)
    S += dSdt * dt
    I += dIdt * dt
    R += dRdt * dt
    print(",".join(str(x) for x in [S, I, R]))
    sys.stdout.flush()
    time.sleep(1)
