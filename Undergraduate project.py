#Simulating Population Dynamics
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Lotka-Volterra model
def lotka_volterra(t, z, alpha, beta, delta, gamma):

    x, y = z

    dx_dt = alpha * x - beta * x * y
    dy_dt = delta * x * y - gamma * y

    return [dx_dt, dy_dt]


# Model parameters
alpha = 0.1    # Prey growth rate
beta = 0.02    # Predation rate
delta = 0.01   # Predator reproduction rate
gamma = 0.1    # Predator death rate

# Initial populations
x0 = 40        # Initial prey population
y0 = 9         # Initial predator population

initial_conditions = [x0, y0]

# Time interval
t_start = 0
t_end = 100
t_values = np.linspace(t_start, t_end, 1000)

# Solve the differential equations
solution = solve_ivp(
    lotka_volterra,
    [t_start, t_end],
    initial_conditions,
    args=(alpha, beta, delta, gamma),
    t_eval=t_values,
    method='RK45'
)

# Extract numerical solutions
time = solution.t
prey = solution.y[0]
predator = solution.y[1]

# Plot population dynamics
plt.figure(figsize=(11, 6))

plt.plot(time, prey, label='Prey Population', linewidth=2)
plt.plot(time, predator, label='Predator Population', linewidth=2)

plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Predator-Prey Population Dynamics')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#The prey population generally increases first, followed by an increase in the predator population. 
As predators become more numerous, the prey population declines, eventually causing the predator population 
to decline as well.
#Phase-plane Analysis
plt.figure(figsize=(8, 7))

plt.plot(prey, predator, linewidth=2)

plt.scatter(x0, y0, color='red', label='Initial condition')

plt.xlabel('Prey Population (x)')
plt.ylabel('Predator Population (y)')

plt.title('Phase Portrait of the Lotka-Volterra Model')

plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
# -The closed trajectories represent periodic predator–prey population cycles.
# -The populations continuously influence each other.
# -The direction of movement around the trajectory shows how the two populations evolve relative to one another.
#Investigating the effects of changing parameters
growth_rates = [0.05, 0.1, 0.2]

plt.figure(figsize=(11, 6))

for a in growth_rates:

    sol = solve_ivp(
        lotka_volterra,
        [0, 100],
        [40, 9],
        args=(a, beta, delta, gamma),
        t_eval=t_values
    )

    plt.plot(
        sol.t,
        sol.y[0],
        label=f'Prey growth rate = {a}'
    )

plt.xlabel('Time')
plt.ylabel('Prey Population')

plt.title('Effect of Prey Growth Rate on Population Dynamics')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
# This experiment allows you to investigate how different reproductive rates influence prey population fluctuations.
#Investigating the relationship between predator and prey populations
initial_conditions_list = [
    [20, 5],
    [40, 9],
    [60, 12],
    [80, 15]
]

plt.figure(figsize=(9, 7))

for initial in initial_conditions_list:

    sol = solve_ivp(
        lotka_volterra,
        [0, 100],
        initial,
        args=(alpha, beta, delta, gamma),
        t_eval=t_values
    )

    plt.plot(
        sol.y[0],
        sol.y[1],
        label=f'Initial populations: {initial}'
    )

plt.xlabel('Prey Population')
plt.ylabel('Predator Population')

plt.title('Phase Portrait Under Different Initial Conditions')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#This experiment demonstrates how different initial population sizes produce different trajectories in the phase plane.
#Numerical equilibrium analysis
# Calculate equilibrium populations

prey_equilibrium = gamma / delta
predator_equilibrium = alpha / beta

print("Equilibrium Analysis")
print("--------------------")

print("Prey equilibrium:", prey_equilibrium)
print("Predator equilibrium:", predator_equilibrium)
#The equilibrium is a stationary solution of the differential equations. 
However, in the classical Lotka–Volterra model, this positive equilibrium is
a neutrally stable centre, not an asymptotically stable equilibrium.
