from collections import deque
from collections import namedtuple
import random
import numpy as np
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class ReplayBuffer():
    def __init__(self,buffer_size,batch_size, n_agents=2):
        self.batch_size = batch_size
        self.memory = deque(maxlen = buffer_size)
        self.batch_size = batch_size
        self.experience = namedtuple("Experience",field_names= ["states", "actions", "rewards", "next_states", "dones"])
        self.num_agents = n_agents
        
    def add(self,state,action,reward,next_state,done):
        e = self.experience(state,action,reward,next_state,done)
        self.memory.append(e)
        
    def sample(self):
        experiences = random.sample(self.memory, k = self.batch_size)
        states = [torch.from_numpy(np.vstack([e.states[index] for e in experiences if e is not None])).float().to(device) for index in range(self.num_agents)]
        actions = [torch.from_numpy(np.vstack([e.actions[index] for e in experiences if e is not None])).float().to(device) for index in range(self.num_agents)]
        rewards = [torch.from_numpy(np.vstack([e.rewards[index] for e in experiences if e is not None])).float().to(device) for index in range(self.num_agents)]
        next_states = [torch.from_numpy(np.vstack([e.next_states[index] for e in experiences if e is not None])).float().to(device) for index in range(self.num_agents)]
        dones = [torch.from_numpy(np.vstack([e.dones[index] for e in experiences if e is not None]).astype(np.uint8)).float().to(device) for index in range(self.num_agents)]
        return (states,actions,rewards,next_states,dones)
    
    def __len__(self):
        return len(self.memory)