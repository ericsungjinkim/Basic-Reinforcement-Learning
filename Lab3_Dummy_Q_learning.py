import gym
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr

def rargmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector==m)[0]
    return pr.choice(indices)

register(
    id='FrozenLake-v3',
    entry_point='gum.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name':'4x4',
            'is_slippery':False}
)
env = gym.make('FrozenLake-v3')

# Intialize table with all zeros
