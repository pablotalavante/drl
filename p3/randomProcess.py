import random
import copy
import numpy as np

RANDOM_SEED = 42

class OrnsteinUhlenbeckNoise():
    def __init__(self, size, mu = 0, theta = 0.10, sigma = 0.2):
        self.mu = mu * np.ones(size)
        self.theta = theta
        self.sigma = sigma
        self.seed = random.seed(RANDOM_SEED)
        self.reset()
        self.size = size
        
    def reset(self):
        self.state = copy.copy(self.mu)
        
    def sample(self):
        x = self.state
        dx = self.theta * (self.mu - x) + self.sigma * np.random.standard_normal(self.size)
        self.state = x + dx        
        return self.state