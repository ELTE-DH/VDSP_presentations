import numpy as np

class DoublePendulum:
    def __init__(self, theta1, theta2, omega1, omega2, l1=1.0, l2=1.0, m1=1.0, m2=1.0, g=9.81, damping=1e-4):
        """
        Initializes the double pendulum with given initial conditions.
        
        Parameters:
        theta1, theta2: Initial angles (in radians)
        omega1, omega2: Initial angular velocities (in radians/sec)
        l1, l2: Lengths of the two links (default 1.0)
        m1, m2: Masses of the two nodes (default 1.0)
        g: Gravitational acceleration (default 9.81 m/s^2)
        damping: Damping coefficient (default 1e-4)
        """
        self.theta1 = theta1
        self.theta2 = theta2
        self.omega1 = omega1
        self.omega2 = omega2
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.g = g
        self.damping = damping

    def _derivatives(self, state):
        """
        Computes the derivatives of the state variables.
        
        Parameters:
        state: A tuple containing (theta1, omega1, theta2, omega2)
        
        Returns:
        derivatives: A tuple containing the derivatives (dtheta1, domega1, dtheta2, domega2)
        """
        theta1, omega1, theta2, omega2 = state
        delta_theta = theta2 - theta1
        
        denominator1 = (self.m1 + self.m2) * self.l1 - self.m2 * self.l1 * np.cos(delta_theta) ** 2
        denominator2 = (self.l2 / self.l1) * denominator1
        
        dtheta1 = omega1
        dtheta2 = omega2

        domega1 = (self.m2 * self.l1 * omega1 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) +
                   self.m2 * self.g * np.sin(theta2) * np.cos(delta_theta) +
                   self.m2 * self.l2 * omega2 ** 2 * np.sin(delta_theta) -
                   (self.m1 + self.m2) * self.g * np.sin(theta1)) / denominator1
                   
        domega2 = (-self.m2 * self.l2 * omega2 ** 2 * np.sin(delta_theta) * np.cos(delta_theta) +
                   (self.m1 + self.m2) * self.g * np.sin(theta1) * np.cos(delta_theta) -
                   (self.m1 + self.m2) * self.l1 * omega1 ** 2 * np.sin(delta_theta) -
                   (self.m1 + self.m2) * self.g * np.sin(theta2)) / denominator2
        
        # Apply damping
        domega1 -= self.damping * omega1
        domega2 -= self.damping * omega2
        
        return dtheta1, domega1, dtheta2, domega2

    def _rk4_step(self, state, dt):
        """
        Helper method to perform a single Runge-Kutta step.
        
        Parameters:
        state: A tuple containing the current state (theta1, omega1, theta2, omega2)
        dt: Time step for the update
        
        Returns:
        delta: A list containing the changes in state variables (dtheta1, domega1, dtheta2, domega2)
        """
        k1 = self._derivatives(state)
        k2 = self._derivatives([state[i] + dt/2*k1[i] for i in range(4)])
        k3 = self._derivatives([state[i] + dt/2*k2[i] for i in range(4)])
        k4 = self._derivatives([state[i] + dt*k3[i] for i in range(4)])
        
        return [
            dt / 6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(4)
        ]

    def step(self, dt):
        """
        Updates the state of the pendulum using the Runge-Kutta method.
        
        Parameters:
        dt: Time step for the update
        
        Returns:
        state: A tuple containing the updated state (theta1, omega1, theta2, omega2)
        """
        state = (self.theta1, self.omega1, self.theta2, self.omega2)
        delta = self._rk4_step(state, dt)
        
        self.theta1 += delta[0]
        self.omega1 += delta[1]
        self.theta2 += delta[2]
        self.omega2 += delta[3]
        
        # Ensure angles remain within [0, 2π]
        self.theta1 %= 2 * np.pi
        self.theta2 %= 2 * np.pi
        
        return self.theta1, self.omega1, self.theta2, self.omega2