# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:23:05 2026

@author: peill
"""

import numpy as np

class BallisticSimulation:
    def __init__(self, v0, alpha):
        self.v0 = v0
        self.alpha = np.deg2rad(alpha)
        self.g = 9.81
        
    def step(self, dt):
        x_t = self.v0 * np.cos(self.alpha) * dt
        y_t = -self.g * dt**2 / 2 + self.v0 * np.sin(self.alpha) * dt
        position_dt = [x_t, y_t]
        
        vx_t = self.v0 * np.cos(self.alpha)
        vy_t = -self.g * dt + self.v0 * np.sin(self.alpha)
        velocity_dt = [vx_t, vy_t]
        
        return position_dt, velocity_dt
    
    def reach(self):
        return(2 * self.v0 * np.sin(self.alpha) / self.g)
    
    def simulate(self):
        position, velocity = [], []

        for dt in np.linspace(0, self.reach(), num=200):
            position_dt, velocity_dt = self.step(dt)
            if position_dt[1] < 0 and dt > 0:
                break
            position.append(position_dt)
            velocity.append(velocity_dt)
        velocity = np.reshape(velocity, (len(velocity), 2))
        position = np.reshape(position, (len(position), 2))
        
        return position, velocity


#%% Test simulation

v0 = 5
alpha = 45

sim = BallisticSimulation(v0, alpha)
position, velocity = sim.simulate()

import matplotlib.pyplot as plt

plt.figure(figsize=(16,9))
plt.title('Position')
plt.plot(position[:,0], position[:,1], color='navy')
plt.ylim(0, 1)
plt.xlim(0, 4)
plt.show()
