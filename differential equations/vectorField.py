# Example of vector field for functions
# Simple harmonic oscillator
# dx/dt = y
# dy/dt = -x

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Create a grid to compute vectors
x, y = np.meshgrid(np.arange(-3, 3, .25), np.arange(-3, 3, .25))

# Create your functions to plot
dxdt = y
dydt = -x

# Put into function for ode solver later if plotting solutions
def f(Y,t):
    x, y = Y
    dYdt = [y, -x]
    return dYdt

# Create figure
fig1, ax1 = plt.subplots()
# Create axis for figure
ax1.set_title('Simple harmonic oscillator')
# Create vectors for vector field
Q = ax1.quiver(x, y, dxdt, dydt, units='width')
# Create type of vectors for vector field
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')

## Plot only vector field figure
## Comment out if you want to put solutions on top
#plt.show()


# Plot solutions to ODE on top of vector field
for y0 in [0, 0.5, 1, 1.5, 2, 2.5]:
    tspan = np.linspace(0, 10, 101)
    initialCondition = [0.0, y0]
    Ysolution = odeint(f,initialCondition, tspan)
    plt.plot(Ysolution[:,0], Ysolution[:,1], 'b-') # path
    plt.plot([Ysolution[0,0]], [Ysolution[0,1]], 'o') # start
    plt.plot([Ysolution[-1,0]], [Ysolution[-1,1]], 's') # end

plt.show()
