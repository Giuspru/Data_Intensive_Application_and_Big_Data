import numpy as np
import matplotlib.pyplot as plt

#Definition of a function that updates percentage of susceptible, infected and recovered population. 
def sir_model( S , I , R, beta, gamma, dt):

    dS = -beta * S * I
    dI =  beta * S * I - gamma * I
    dR = gamma * I

    S_next = S + (dS * dt)
    I_next = I + (dI * dt)
    R_next = R + (dR * dt)

    return S_next, I_next, R_next

def simulate_sir(S0, I0, R0, beta, gamma, dt, T):

    N = int(T/dt) #Definition of time steps we want to simulate

    S, I, R = np.zeros(N), np.zeros(N), np.zeros(N) #Inizialization of three arrays, each one will be filled with percentage of susceptible, infected and recovered population

    for t in range(1,N):
        S[t], I[t], R[t] = sir_model(S[t-1], I[t-1], R[t-1], beta, gamma, dt)

    return S, I, R


def plot_sir(S, I, R, dt, T):
    """Plots the SIR model dynamics."""
    time = np.linspace(0, T, len(S))
    plt.figure(figsize=(10, 5))
    plt.plot(time, S, label='Susceptible', color='blue')
    plt.plot(time, I, label='Infected', color='red')
    plt.plot(time, R, label='Recovered', color='green')
    plt.xlabel("Time")
    plt.ylabel("Population Fraction")
    plt.title("SIR Model Simulation")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":

    # Initial conditions
    S0 = 0.999999 #Innitial fraction of susceptible pupolation
    I0 = 0.000001 #Initial fraction of infected population
    R0 = 0.0 # Initial fraction of recovered population
    beta = 0.3 #Infection rate
    gamma = 0.1 #Recovery rate
    dt = 0.01 #Time step
    T = 1000 #Total time


    S, I, R = simulate_sir(S0, I0, R0, beta, gamma, dt, T)
    plot_sir(S, I, R, dt, T)
