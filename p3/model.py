import torch.nn as nn
import torch.nn.functional as F
import torch

RANDOM_SEED = 42               

class Actor(nn.Module):    
    def __init__(self, s_size, a_size, fc1_units = 256, fc2_units = 128):

        super(Actor,self).__init__()
        self.seed = torch.manual_seed(RANDOM_SEED)
        
        self.fc1 = nn.Linear(s_size ,fc1_units)
        self.fc2 = nn.Linear(fc1_units,fc2_units)
        self.fc3 = nn.Linear(fc2_units,a_size)
        
        
    def forward(self,state):
        """Build an actor (policy) network that maps states -> actions."""
        a = F.relu(self.fc1(state))
        a = F.relu(self.fc2(a))
        return F.tanh(self.fc3(a))
    

class Critic(nn.Module):
    
    def __init__(self, state_size, action_size, num_agents=2, fc1_units = 512, fc2_units = 256):
        super(Critic,self).__init__()
        self.seed = torch.manual_seed(RANDOM_SEED)
        
        self.fc1 = nn.Linear((state_size + action_size) * num_agents,fc1_units)
        self.fc2 = nn.Linear(fc1_units,fc2_units)
        self.fc3 = nn.Linear(fc2_units,1)
        self.bn = nn.BatchNorm1d(fc1_units)

        
    def forward(self,state,action):
        ca = torch.cat((state,action.float()),dim = 1)
        a = F.leaky_relu(self.fc1(ca))
        a = self.bn(a)
        a = F.leaky_relu(self.fc2(a))
        return self.fc3(a)